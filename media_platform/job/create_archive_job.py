from __future__ import annotations

from media_platform.job.job import Job
from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.service.source import Source


class ArchiveType:
    zip = 'zip'
    tar = 'tar'
    tar_gz = 'tar.gz'
    tar_bz2 = 'tar.bz2'

    @classmethod
    def has_value(cls, value):
        return value in [cls.zip, cls.tar, cls.tar_gz, cls.tar_bz2]


class ArchiveSource(Source):
    def __init__(self, path: str = None, file_id: str = None, path_in_archive: str = None):
        super().__init__(path, file_id)

        self.path_in_archive = path_in_archive

    @classmethod
    def deserialize(cls, data: dict) -> ArchiveSource:
        return ArchiveSource(data.get('path'), data.get('fileId'), data.get('pathInArchive'))

    def serialize(self) -> dict:
        data = super().serialize()
        data['pathInArchive'] = self.path_in_archive if self.path_in_archive else None

        return data

    @classmethod
    def from_source(cls, source: Source) -> ArchiveSource:
        return ArchiveSource(source.path, source.file_id)


class CreateArchiveSpecification(Specification):
    def __init__(self, sources: [Source or ArchiveSource], destination: Destination,
                 archive_type: ArchiveType = ArchiveType.zip):
        self.sources = sources
        self.destination = destination
        self.archive_type = archive_type

    @classmethod
    def deserialize(cls, data: dict) -> CreateArchiveSpecification:
        sources_data = data.get('sources')
        sources = [ArchiveSource.deserialize(source_info) for source_info in sources_data if source_info]

        return CreateArchiveSpecification(sources,
                                          Destination.deserialize(data['destination']),
                                          data['archiveType'])

    def serialize(self) -> dict:
        return {
            'sources': [source.serialize() for source in self.sources if source],
            'destination': self.destination.serialize(),
            'archiveType': self.archive_type
        }


class CreateArchiveJob(Job):
    type = JobType.create_archive
    specification_type = CreateArchiveSpecification
