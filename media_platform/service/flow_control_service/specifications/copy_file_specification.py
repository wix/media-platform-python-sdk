from __future__ import annotations

from media_platform.service.destination import Destination
from media_platform.job.specification import Specification


class CopyFileSpecification(Specification):
    def __init__(self, destination: Destination):
        self.destination = destination

    def serialize(self) -> dict:
        return {
            'destination': self.destination.serialize()
        }

    @classmethod
    def deserialize(cls, data: dict) -> CopyFileSpecification:
        return cls(Destination.deserialize(data['destination']))
