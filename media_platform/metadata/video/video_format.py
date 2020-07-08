from __future__ import annotations

from media_platform.lang.serialization import Deserializable


class VideoFormat(Deserializable):
    def __init__(self, long_name: str = None, bitrate: int = None, duration: int = None, size: int = None):
        super(VideoFormat, self).__init__()
        self.long_name = long_name
        self.duration = duration
        self.bitrate = int(bitrate) if bitrate else None
        self.size = int(size) if size else None

    @classmethod
    def deserialize(cls, data: dict) -> VideoFormat:
        return VideoFormat(data.get('formatLongName'),
                           data.get('bitrate'),
                           data.get('duration'),
                           data.get('size'))

    def serialize(self) -> dict:
        return {
            'formatLongName': self.long_name,
            'duration': self.duration,
            'bitrate': self.bitrate,
            'size': self.size,
        }
