from media_platform.lang.serialization import Deserializable


class VideoStream(Deserializable):
    def __init__(self, index, width, height, avg_frame_rate, r_frame_rate, display_aspect_ratio, sample_aspect_ratio,
                 rotate, duration, bitrate, codec_tag, codec_name, codec_long_name, pixel_format):
        # type: (int, int, int, str, str, str, str, int, int, int, str, str, str, str) -> None

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

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoStream
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
                           data.get('pixelFormat'))
