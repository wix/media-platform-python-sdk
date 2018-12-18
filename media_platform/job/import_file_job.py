from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


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
