from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable, Deserializable


class VideoSpecification(Specification):
    def __init__(self, codec, resolution=None, frame_rate=None):
        # type: (VideoCodec, Resolution or None, float) -> None
        self.codec = codec
        self.resolution = resolution
        self.frame_rate = frame_rate

    @classmethod
    def deserialize(cls, data):
        codec = VideoCodec.deserialize(data['codec'])
        resolution = Resolution.deserialize(data.get('resolution')) if data.get('resolution') else None

        return VideoSpecification(codec, resolution, data.get('frameRate'))

    def serialize(self):
        return {
            'codec': self.codec.serialize(),
            'resolution': self.resolution.serialize() if self.resolution else None,
            'frameRate': self.frame_rate
        }

    def validate(self):
        if self.resolution:
            self.resolution.validate()


class Resolution(Serializable, Deserializable):
    def __init__(self, width=None, height=None):
        # type: (int, int) -> None
        self.width = width
        self.height = height

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Resolution
        return Resolution(data.get('width'), data.get('height'))

    def serialize(self):
        # type: () -> dict
        return {
            'width': self.width,
            'height': self.height
        }

    def validate(self):
        if self.width and self.width % 2:
            raise ValueError('resolution width %s not divisible by 2' % self.width)

        if self.height and self.height % 2:
            raise ValueError('resolution height %s not divisible by 2' % self.height)


class VideoCodec(Serializable, Deserializable):
    def __init__(self, name, profile, level, crf, max_rate):
        # type: (str, str, str, int, float) -> None
        self.name = name
        self.profile = profile
        self.level = level
        self.crf = crf
        self.max_rate = max_rate

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoCodec
        return VideoCodec(data['name'], data['profile'], data['level'], data['crf'], data['maxRate'])

    def serialize(self):
        # type: () -> dict
        return {
            'name': self.name,
            'profile': self.profile,
            'level': self.level,
            'crf': self.crf,
            'maxRate': self.max_rate
        }
