from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.job.job import Job
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class ImportFileSpecification(Specification):
    def __init__(self, source_url, destination):
        # type: (str, Destination) -> None
        super(ImportFileSpecification, self).__init__()

        self.source_url = source_url
        self.destination = destination

    def serialize(self):
        # type: () -> dict
        return {
            'sourceUrl': self.source_url,
            'destination': self.destination.serialize()
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImportFileSpecification
        destination = Destination.deserialize(data['destination'])

        return ImportFileSpecification(data['sourceUrl'], destination)


class ImportFileJob(Job):
    type = 'urn:job:import.file'
    specification_type = ImportFileSpecification
