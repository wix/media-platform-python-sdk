from __future__ import annotations

from media_platform.service.destination import Destination
from typing import Dict

from media_platform.lang.serialization import Deserializable, Serializable


class StreamDVR(Deserializable, Serializable):
    def __init__(self, destination: Destination):
        self.destination = destination

    @classmethod
    def deserialize(cls, data: dict) -> StreamDVR:
        destination = Destination.deserialize(data['destination'])

        return cls(destination)

    def serialize(self) -> Dict:
        return {
            'destination': self.destination.serialize()
        }
