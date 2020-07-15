from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.metadata.audio.audio_stream import AudioStream
from media_platform.metadata.video.transparency import Transparency
from media_platform.metadata.video.video_format import VideoFormat
from media_platform.metadata.video.video_stream import VideoStream


class VideoBasic(Serializable, Deserializable):
    def __init__(self, video_streams: [VideoStream], audio_streams: [AudioStream], video_format: VideoFormat = None,
                 video_interlaced: bool = False, video_tbr: dict = None, transparency: Transparency = None):
        self.video_streams = video_streams or []
        self.audio_streams = audio_streams or []
        self.video_format = video_format
        self.video_interlaced = video_interlaced
        self.video_tbr = video_tbr
        self.transparency = transparency

    @classmethod
    def deserialize(cls, data: dict) -> VideoBasic:
        video_streams = [VideoStream.deserialize(stream) for stream in data['videoStreams']]
        audio_streams = [AudioStream.deserialize(stream) for stream in data['audioStreams']]
        video_format = VideoFormat.deserialize(data['format']) if data.get('format') else None

        return VideoBasic(video_streams, audio_streams, video_format, data.get('interlaced'),
                          data.get('tbr'), data.get('transparency'))

    def serialize(self):
        return {
            'videoStreams': [video_stream.serialize() for video_stream in self.video_streams],
            'audioStreams': [audio_stream.serialize() for audio_stream in self.audio_streams],
            'format': self.video_format.serialize() if self.video_format else None,
            'interlaced': self.video_interlaced,
            'tbr': self.video_tbr,
            'transparency': self.transparency
        }
