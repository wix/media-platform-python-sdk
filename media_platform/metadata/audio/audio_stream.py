from media_platform.lang.serialization import Deserializable


class AudioStream(Deserializable):
    def __init__(self, index, duration, bitrate, codec_tag, codec_name, codec_long_name, sample_rate, channels,
                 channel_layout):
        self.index = int(index)
        self.duration = duration
        self.bitrate = int(bitrate) if bitrate else None
        self.codec_tag = codec_tag
        self.codec_name = codec_name
        self.codec_long_name = codec_long_name
        self.sample_rate = int(sample_rate) if sample_rate else None
        self.channel_layout = channel_layout
        self.channels = int(channels) if channels else None

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioStream
        return AudioStream(data.get('index'), data.get('duration'), data.get('bitrate'),
                           data.get('codecTag'), data.get('codecName'), data.get('codecLongName'),
                           data.get('sampleRate'), data.get('channels'), data.get('channelLayout'))

    def serialize(self):
        return {
            'index': self.index,
            'duration': self.duration,
            'bitrate': self.bitrate,
            'codecTag': self.codec_tag,
            'codecName': self.codec_name,
            'codecLongName': self.codec_long_name,
            'sampleRate': self.sample_rate,
            'channelLayout': self.channel_layout,
            'channels': self.channels
        }
