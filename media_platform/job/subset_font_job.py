from __future__ import annotations

from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


class SubsetFontSpecification(Specification):
    def __init__(self, destination: Destination, language_code: str = None):
        self.destination = destination
        self.language_code = language_code

    @classmethod
    def deserialize(cls, data: dict) -> SubsetFontSpecification:
        destination = Destination.deserialize(data['destination'])

        return SubsetFontSpecification(destination, data.get('languageCode'))

    def serialize(self) -> dict:
        return {
            'destination': self.destination.serialize(),
            'languageCode': self.language_code,
        }


class SubsetFontJob(Job):
    type = 'urn:job:text.font.subset'
    specification_type = SubsetFontSpecification
