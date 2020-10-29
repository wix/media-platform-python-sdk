from __future__ import annotations

from media_platform.lang.serialization import Deserializable, Serializable


class VideoStream(Serializable, Deserializable):
    def __init__(self, index: int, width: int, height: int, avg_frame_rate: str, r_frame_rate: str,
                 display_aspect_ratio: str, sample_aspect_ratio: str,
                 rotate: int, duration: int, bitrate: int, codec_tag: str, codec_name: str, codec_long_name: str,
                 pixel_format: str, field_order: str = None, disposition: [str] = None):
        self.index = int(index)
        self.width = int(width) if width else None
        self.height = int(height) if height else None
        self.avg_frame_rate = avg_frame_rate
        self.r_frame_rate = r_frame_rate
        self.display_aspect_ratio = display_aspect_ratio
        self.sample_aspect_ratio = sample_aspect_ratio
        self.rotate = int(rotate) if rotate is not None else None
        self.duration = duration
        self.bitrate = int(bitrate) if bitrate else None
        self.codec_tag = codec_tag
        self.codec_name = codec_name
        self.codec_long_name = codec_long_name
        self.pixel_format = pixel_format
        self.field_order = field_order
        self.disposition = disposition or []

    @classmethod
    def deserialize(cls, data: dict) -> VideoStream:
        return VideoStream(data.get('index'),
                           data.get('width'),
                           data.get('height'),
                           data.get('avgFrameRate'),
                           data.get('rFrameRate'),
                           data.get('displayAspectRatio'),
                           data.get('sampleAspectRatio', '1:1'),
                           data.get('rotate'),
                           data.get('duration'),
                           data.get('bitrate'),
                           data.get('codecTag'),
                           data.get('codecName'),
                           data.get('codecLongName'),
                           data.get('pixelFormat'),
                           data.get('fieldOrder'),
                           data.get('disposition')
                           )

    def serialize(self) -> dict:
        return {
            'index': self.index,
            'width': self.width,
            'height': self.height,
            'avgFrameRate': self.avg_frame_rate,
            'rFrameRate': self.r_frame_rate,
            'displayAspectRatio': self.display_aspect_ratio,
            'sampleAspectRatio': self.sample_aspect_ratio,
            'rotate': self.rotate,
            'duration': self.duration,
            'bitrate': self.bitrate,
            'codecTag': self.codec_tag,
            'codecName': self.codec_name,
            'codecLongName': self.codec_long_name,
            'pixelFormat': self.pixel_format,
            'fieldOrder': self.field_order,
            'disposition': self.disposition
        }
