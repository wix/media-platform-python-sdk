from media_platform.lang.serialization import Deserializable


class AudioFormat(Deserializable):
    def __init__(self, long_name=None, bitrate=None, duration=None, size=None):
        # type: (str, int or None, int or None, int or None) -> None
        super(AudioFormat, self).__init__()
        self.long_name = long_name
        self.duration = duration
        self.bitrate = int(bitrate) if bitrate else None
        self.size = int(size) if size else None

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioFormat
        return AudioFormat(data.get('formatLongName'),
                           data.get('bitrate'),
                           data.get('duration'),
                           data.get('size'))

    def serialize(self):
        # type: () -> dict
        return {
            'formatLongName': self.long_name,
            'duration': self.duration,
            'bitrate': self.bitrate,
            'size': self.size,
        }
