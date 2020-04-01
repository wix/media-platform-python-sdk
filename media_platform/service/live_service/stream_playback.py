from media_platform.lang.serialization import Deserializable, Serializable


class PackageName(object):
    hls = 'hls'
    dash = 'dash'


class StreamPlayback(Serializable, Deserializable):
    def __init__(self, package_name, path):
        # type: (PackageName, str) -> None

        self.package_name = package_name
        self.path = path

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> StreamPlayback

        return cls(data['packageName'], data['path'])

    def serialize(self):
        # type: () -> dict

        return {
            'packageName': self.package_name,
            'path': self.path
        }
