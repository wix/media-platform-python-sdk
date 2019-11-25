from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


class SubsetFontSpecification(Specification):
    def __init__(self, destination, language_code=None):
        # type: (Destination, str) -> None
        super(SubsetFontSpecification, self).__init__()
        self.destination = destination

        self.language_code = language_code

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> SubsetFontSpecification
        destination = Destination.deserialize(data['destination'])

        return SubsetFontSpecification(destination, data.get('languageCode'))

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize(),
            'languageCode': self.language_code,
        }


class SubsetFontJob(Job):
    type = 'urn:job:text.font.subset'
    specification_type = SubsetFontSpecification
