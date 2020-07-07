from media_platform.lang.serialization import Deserializable, Serializable


class PackageName:
    hls = 'hls'
    dash = 'dash'


class StreamPlayback(Serializable, Deserializable):
    def __init__(self, package_name: PackageName, path: str):
        self.package_name = package_name
        self.path = path

    @classmethod
    def deserialize(cls, data: dict):
        return cls(data['packageName'], data['path'])

    def serialize(self) -> dict:
        return {
            'packageName': self.package_name,
            'path': self.path
        }
