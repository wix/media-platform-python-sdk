from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class GeoLocation(Serializable, Deserializable):
    def __init__(self, latitude: float = None, longitude: float = None, ip_address: str = None, country: str = None,
                 city: str = None):
        self.latitude = latitude
        self.longitude = longitude
        self.ip_address = ip_address
        self.country = country
        self.city = city

    def serialize(self) -> dict:
        return {
            'coordinates': {
                'latitude': self.latitude,
                'longitude': self.longitude
            },
            'ipAddress': self.ip_address,
            'country': self.country,
            'city': self.city
        }

    @classmethod
    def deserialize(cls, data: dict) -> GeoLocation:
        coordinates_data = data.get('coordinates') or {}
        return cls(coordinates_data.get('latitude'),
                   coordinates_data.get('longitude'),
                   data.get('ipAddress'),
                   data.get('country'),
                   data.get('city'))
