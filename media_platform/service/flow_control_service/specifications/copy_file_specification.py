from media_platform.service.destination import Destination
from media_platform.job.specification import Specification


class CopyFileSpecification(Specification):
    def __init__(self, destination):
        # type: (Destination) -> None
        self.destination = destination

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize()
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> CopyFileSpecification
        return cls(Destination.deserialize(data['destination']))
