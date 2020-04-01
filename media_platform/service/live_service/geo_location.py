from media_platform.lang.serialization import Serializable, Deserializable


class GeoLocation(Serializable, Deserializable):
    def __init__(self, latitude=None, longitude=None, ip_address=None, country=None, city=None):
        # type: (float, float, str, str, str) -> None

        self.latitude = latitude
        self.longitude = longitude
        self.ip_address = ip_address
        self.country = country
        self.city = city

    def serialize(self):
        # type: () -> dict

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
    def deserialize(cls, data):
        # type: (dict) -> GeoLocation

        coordinates_data = data.get('coordinates') or {}
        return cls(coordinates_data.get('latitude'),
                   coordinates_data.get('longitude'),
                   data.get('ipAddress'),
                   data.get('country'),
                   data.get('city'))
