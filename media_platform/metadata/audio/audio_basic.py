from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.metadata.audio.audio_format import AudioFormat
from media_platform.metadata.audio.audio_stream import AudioStream


class AudioBasic(Serializable, Deserializable):
    def __init__(self, audio_streams, audio_format=None):
        # type: ([AudioStream], AudioFormat) -> None

        self.audio_streams = audio_streams or []
        self.audio_format = audio_format

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioBasic
        audio_streams = [AudioStream.deserialize(stream) for stream in data['audioStreams']]
        audio_format = AudioFormat.deserialize(data['format']) if data.get('format') else None

        return AudioBasic(audio_streams, audio_format)

    def serialize(self):
        return {
            'audioStreams': [audio_stream.serialize() for audio_stream in self.audio_streams],
            'format': self.audio_format.serialize() if self.audio_format else None
        }
