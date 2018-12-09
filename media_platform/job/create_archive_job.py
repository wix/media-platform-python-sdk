from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class ArchiveType(object):
    zip = 'zip'
    tar = 'tar'
    tar_gz = 'tar.gz'
    tar_bz2 = 'tar.bz2'

    @classmethod
    def has_value(cls, value):
        return value in [cls.zip, cls.tar, cls.tar_gz, cls.tar_bz2]


class ArchiveSource(Source):
    def __init__(self, path=None, file_id=None, path_in_archive=None):
        # type: (str, str, str) -> None
        super(ArchiveSource, self).__init__(path, file_id)

        self.path_in_archive = path_in_archive

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ArchiveSource
        return ArchiveSource(data.get('path'), data.get('fileId'), data.get('pathInArchive'))

    def serialize(self):
        # type: () -> dict
        data = super(ArchiveSource, self).serialize()
        data['pathInArchive'] = self.path_in_archive if self.path_in_archive else None

        return data

    @classmethod
    def from_source(cls, source):
        # type: (Source) -> ArchiveSource
        return ArchiveSource(source.path, source.file_id)


class CreateArchiveSpecification(Specification):
    def __init__(self, sources, destination, archive_type=ArchiveType.zip):
        # type: ([Source or ArchiveSource], Destination, ArchiveType) -> None

        self.sources = sources
        self.destination = destination
        self.archive_type = archive_type

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> CreateArchiveSpecification
        sources_data = data.get('sources')
        sources = [ArchiveSource.deserialize(source_info) for source_info in sources_data if source_info]

        return CreateArchiveSpecification(sources,
                                          Destination.deserialize(data['destination']),
                                          data['archiveType'])

    def serialize(self):
        # type: () -> dict
        return {
            'sources': [source.serialize() for source in self.sources if source],
            'destination': self.destination.serialize(),
            'archiveType': self.archive_type
        }


class CreateArchiveJob(Job):
    type = 'urn:job:archive.create'

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(CreateArchiveJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                               callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> CreateArchiveJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = CreateArchiveSpecification.deserialize(data['specification'])
        if data.get('result'):
            # todo: result payload is FileDescriptor
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
