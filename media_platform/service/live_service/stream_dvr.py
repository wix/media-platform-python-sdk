from media_platform.service.destination import Destination
from typing import Dict

from media_platform.lang.serialization import Deserializable, Serializable


class StreamDVR(Deserializable, Serializable):
    def __init__(self, destination):
        # type: (Destination) -> None

        self.destination = destination

    @classmethod
    def deserialize(cls, data):
        # type: (Dict) -> StreamDVR

        destination = Destination.deserialize(data['destination'])

        return cls(destination)

    def serialize(self):
        # type: () -> Dict

        return {
            'destination': self.destination.serialize()
        }
