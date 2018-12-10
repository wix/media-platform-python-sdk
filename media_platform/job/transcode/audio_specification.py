from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable, Deserializable


class AudioSpecification(Specification):
    def __init__(self, codec, channels=None, sampling=None):
        # type: (AudioCodec, Channels, AudioSampling) -> None

        self.codec = codec
        self.channels = channels
        self.sampling = sampling

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioSpecification

        codec = AudioCodec.deserialize(data['codec'])

        sampling_info = data.get('sampling')
        sampling = AudioSampling.deserialize(sampling_info) if sampling_info else None

        return AudioSpecification(codec, data.get('channels'), sampling)

    def serialize(self):
        return {
            'codec': self.codec.serialize(),
            'channels': self.channels,
            'sampling': self.sampling.serialize() if self.sampling else None
        }

    def validate(self):
        if self.channels and not Channels.has_value(self.channels):
            raise ValueError('Channels must be one of %s' % ', '.join(Channels.values))


class Channels(object):
    stereo = 'stereo'
    mono = 'mono'
    joint = 'joint'

    values = [stereo, mono, joint]

    @classmethod
    def has_value(cls, value):
        # type: (str) -> bool
        return value in cls.values


class AudioCodec(Serializable, Deserializable):
    def __init__(self, name, cbr=None, abr=None, vbr=None, profile=None):
        # type: (str, float, float, float, AudioProfile) -> None

        self.name = name
        self.cbr = cbr
        self.abr = abr
        self.vbr = vbr
        self.profile = profile

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioCodec
        profile_info = data.get('profile')
        profile = AudioProfile.deserialize(profile_info) if profile_info else None

        return AudioCodec(data['name'], data.get('cbr'), data.get('abr'), data.get('vbr'), profile)

    def serialize(self):
        # type: () -> dict
        return {
            'name': self.name,
            'cbr': self.cbr,
            'abr': self.abr,
            'vbr': self.vbr,
            'profile': self.profile.serialize() if self.profile else None
        }


class AudioSampling(Serializable, Deserializable):
    def __init__(self, rate, size):
        # type: (int, int) -> None

        self.rate = rate
        self.size = size

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioSampling
        return AudioSampling(data.get('rate'), data.get('size'))

    def serialize(self):
        # type: () -> dict
        return {
            'rate': self.rate,
            'size': self.size
        }


class AudioProfile(Serializable, Deserializable):
    def __init__(self, name, rate):
        # type: (str, float) -> None
        self.name = name
        self.rate = rate

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioProfile
        return AudioProfile(data['name'], data['rate'])

    def serialize(self):
        # type: () -> dict
        return {
            'name': self.name,
            'rate': self.rate
        }
