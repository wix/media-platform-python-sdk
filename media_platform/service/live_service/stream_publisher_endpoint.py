from typing import Dict

from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.live_service.geo_location import GeoLocation
from media_platform.service.live_service.stream_protocol import StreamProtocol


class StreamPublishEndpoint(Serializable, Deserializable):
    def __init__(self, url: str, protocol: StreamProtocol, geo: GeoLocation = None):
        self.url = url
        self.protocol = protocol
        self.geo = geo

    def serialize(self) -> Dict:
        return {
            'url': self.url,
            'protocol': self.protocol,
            'geo': self.geo.serialize() if self.geo else None
        }

    @classmethod
    def deserialize(cls, data: dict):
        geo = GeoLocation.deserialize(data['geo']) if data.get('geo') else None

        return cls(data['url'], data['protocol'], geo)
