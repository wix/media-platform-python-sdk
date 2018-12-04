from media_platform.lang.serialization import Deserializable
from media_platform.metadata.audio.audio_stream import AudioStream
from media_platform.metadata.video.video_format import VideoFormat
from media_platform.metadata.video.video_stream import VideoStream


class VideoBasic(Deserializable):
    def __init__(self, video_streams, audio_streams, video_format=None, video_interlaced=False, video_tbr=None):
        # type: ([VideoStream], [AudioStream], VideoFormat, bool, dict) -> None

        self.video_streams = video_streams or []
        self.audio_streams = audio_streams or []
        self.video_format = video_format
        self.video_interlaced = video_interlaced
        self.video_tbr = video_tbr

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoBasic
        video_streams = [VideoStream.deserialize(stream) for stream in data['videoStreams']]
        audio_streams = [AudioStream.deserialize(stream) for stream in data['audioStreams']]
        video_format = VideoFormat.deserialize(data['format']) if data.get('format') else None

        return VideoBasic(video_streams, audio_streams, video_format, data.get('interlaced'),
                          data.get('tbr'))
