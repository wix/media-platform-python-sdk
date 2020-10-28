from __future__ import annotations

from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable, Deserializable


class VideoSpecification(Specification):
    def __init__(self, codec: VideoCodec, resolution: Resolution = None, frame_rate: float = None,
                 filters: [VideoFilter] = None, frame_rate_fraction: str = None):
        self.codec = codec
        self.resolution = resolution
        self.frame_rate = frame_rate
        self.filters = filters
        self.frame_rate_fraction = frame_rate_fraction

    @classmethod
    def deserialize(cls, data) -> VideoSpecification:
        codec = VideoCodec.deserialize(data['codec'])

        resolution = Resolution.deserialize(data.get('resolution')) if data.get('resolution') else None

        filters_data = data.get('filters')
        filters = [ImageFilter.deserialize(f) for f in filters_data] if filters_data else None

        return VideoSpecification(codec, resolution, data.get('frameRate'), filters, data.get('frameRateFraction'))

    def serialize(self) -> dict:
        data = {
            'codec': self.codec.serialize(),
            'resolution': self.resolution.serialize() if self.resolution else None,
            'filters': [f.serialize() for f in self.filters] if self.filters else None,
        }

        if self.frame_rate_fraction:
            data['frameRateFraction'] = self.frame_rate_fraction
        else:
            data['frameRate'] = self.frame_rate

        return data

    def validate(self):
        if self.resolution:
            self.resolution.validate()


class Resolution(Serializable, Deserializable):
    def __init__(self, width: int = None, height: int = None, scaling: VideoScaling = None,
                 sample_aspect_ratio: str = None):
        self.width = width
        self.height = height
        self.scaling = scaling
        self.sample_aspect_ratio = sample_aspect_ratio  # defaults to '1:1'

    @classmethod
    def deserialize(cls, data: dict) -> Resolution:
        scaling_data = data.get('scaling')
        scaling = VideoScaling.deserialize(scaling_data) if scaling_data else None

        return Resolution(data.get('width'), data.get('height'), scaling, data.get('sampleAspectRatio'))

    def serialize(self) -> dict:
        return {
            'width': self.width,
            'height': self.height,
            'scaling': self.scaling.serialize() if self.scaling else None,
            'sampleAspectRatio': self.sample_aspect_ratio
        }

    def validate(self):
        if self.width and self.width % 2:
            raise ValueError('resolution width %s not divisible by 2' % self.width)

        if self.height and self.height % 2:
            raise ValueError('resolution height %s not divisible by 2' % self.height)


class VideoCodec(Serializable, Deserializable):
    def __init__(self, name: str, profile: str, level: str, crf: int, max_rate: float, gop: GOP = None,
                 preset: str = None):
        self.name = name
        self.profile = profile
        self.level = level
        self.crf = crf
        self.max_rate = max_rate
        self.gop = gop
        self.preset = preset

    @classmethod
    def deserialize(cls, data: dict) -> VideoCodec:
        gop_data = data.get('gop')
        gop = GOP.deserialize(gop_data) if gop_data else None

        return VideoCodec(data['name'], data['profile'], data['level'], data['crf'], data['maxRate'], gop,
                          data.get('preset'))

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'profile': self.profile,
            'level': self.level,
            'crf': self.crf,
            'maxRate': self.max_rate,
            'gop': self.gop.serialize() if self.gop else None,
            'preset': self.preset
        }


class GOP(Serializable, Deserializable):
    def __init__(self, scene_cut: int, key_interval: int, min_key_interval: int, b_frames: int, b_pyramid: int,
                 b_adapt: int, ref_frame: int):
        self.scene_cut = scene_cut
        self.key_interval = key_interval
        self.min_key_interval = min_key_interval
        self.b_frames = b_frames
        self.b_pyramid = b_pyramid
        self.b_adapt = b_adapt
        self.ref_frame = ref_frame

    @classmethod
    def deserialize(cls, data: dict) -> GOP:
        return cls(
            data['sceneCut'],
            data['keyInterval'],
            data['minKeyInterval'],
            data['bFrames'],
            data['bPyramid'],
            data['bAdapt'],
            data['refFrame']
        )

    def serialize(self) -> dict:
        return {
            'sceneCut': self.scene_cut,
            'keyInterval': self.key_interval,
            'minKeyInterval': self.min_key_interval,
            'bFrames': self.b_frames,
            'bPyramid': self.b_pyramid,
            'bAdapt': self.b_adapt,
            'refFrame': self.ref_frame
        }


class VideoScaling(Serializable, Deserializable):
    def __init__(self, algorithm):
        self.algorithm = algorithm

    @classmethod
    def deserialize(cls, data: dict) -> VideoScaling:
        return cls(data['algorithm'])

    def serialize(self) -> dict:
        return {
            'algorithm': self.algorithm
        }


class VideoFilterName:
    unsharp = 'unsharp'
    make_wix_transparent = 'makeWixTransparent'


class VideoFilter(Serializable, Deserializable):
    def __init__(self, name: VideoFilterName, settings: dict = None):
        self.name = name  # 'unsharp'
        self.settings = settings or {}  # '{"value": "5:5:0.5:3:3:0.0"}'

    @classmethod
    def deserialize(cls, data: dict) -> ImageFilter:
        return cls(data['name'], data.get('settings'))

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'settings': self.settings
        }


ImageFilter = VideoFilter
ImageScaling = VideoScaling
