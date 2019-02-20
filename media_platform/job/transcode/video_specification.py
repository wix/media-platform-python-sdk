from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable, Deserializable


class VideoSpecification(Specification):
    def __init__(self, codec, resolution=None, frame_rate=None, filters=None):
        # type: (VideoCodec, Resolution or None, float, [ImageFilter] or None) -> None
        self.codec = codec
        self.resolution = resolution
        self.frame_rate = frame_rate
        self.filters = filters

    @classmethod
    def deserialize(cls, data):
        codec = VideoCodec.deserialize(data['codec'])

        resolution = Resolution.deserialize(data.get('resolution')) if data.get('resolution') else None

        filters_data = data.get('filters')
        filters = [ImageFilter.deserialize(f) for f in filters_data] if filters_data else None

        return VideoSpecification(codec, resolution, data.get('frameRate'), filters)

    def serialize(self):
        return {
            'codec': self.codec.serialize(),
            'resolution': self.resolution.serialize() if self.resolution else None,
            'frameRate': self.frame_rate,
            'filters': [f.serialize() for f in self.filters] if self.filters else None
        }

    def validate(self):
        if self.resolution:
            self.resolution.validate()


class Resolution(Serializable, Deserializable):
    def __init__(self, width=None, height=None, scaling=None, sample_aspect_ratio=None):
        # type: (int, int, ImageScaling or None, str or None) -> None
        self.width = width
        self.height = height

        self.scaling = scaling
        self.sample_aspect_ratio = sample_aspect_ratio  # defaults to '1:1'

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Resolution
        scaling_data = data.get('scaling')
        scaling = ImageScaling.deserialize(scaling_data) if scaling_data else None

        return Resolution(data.get('width'), data.get('height'), scaling, data.get('sampleAspectRatio'))

    def serialize(self):
        # type: () -> dict
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
    def __init__(self, name, profile, level, crf, max_rate, gop=None, preset=None):
        # type: (str, str, str, int, float, GOP or None, str or None) -> None
        self.name = name
        self.profile = profile
        self.level = level
        self.crf = crf
        self.max_rate = max_rate
        self.gop = gop
        self.preset = preset

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoCodec
        gop_data = data.get('gop')
        gop = GOP.deserialize(gop_data) if gop_data else None

        return VideoCodec(data['name'], data['profile'], data['level'], data['crf'], data['maxRate'], gop,
                          data.get('preset'))

    def serialize(self):
        # type: () -> dict
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
    def __init__(self, scene_cut, key_interval, min_key_interval, b_frames, b_pyramid, b_adapt, ref_frame):
        # type: (int or None, int or None, int or None, int or None, int or None, int or None, int or None) -> None
        super(GOP, self).__init__()

        self.scene_cut = scene_cut

        self.key_interval = key_interval
        self.min_key_interval = min_key_interval

        self.b_frames = b_frames
        self.b_pyramid = b_pyramid
        self.b_adapt = b_adapt

        self.ref_frame = ref_frame

    @classmethod
    def deserialize(cls, data):
        return cls(
            data['sceneCut'],
            data['keyInterval'],
            data['minKeyInterval'],
            data['bFrames'],
            data['bPyramid'],
            data['bAdapt'],
            data['refFrame']
        )

    def serialize(self):
        return {
            'sceneCut': self.scene_cut,
            'keyInterval': self.key_interval,
            'minKeyInterval': self.min_key_interval,
            'bFrames': self.b_frames,
            'bPyramid': self.b_pyramid,
            'bAdapt': self.b_adapt,
            'refFrame': self.ref_frame
        }


class ImageScaling(Serializable, Deserializable):
    def __init__(self, algorithm):
        super(ImageScaling, self).__init__()

        self.algorithm = algorithm

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageScaling
        return cls(data['algorithm'])

    def serialize(self):
        # type: () -> dict
        return {
            'algorithm': self.algorithm
        }


class ImageFilter(Serializable, Deserializable):
    def __init__(self, name, settings):
        # type: (str, dict) -> None
        super(ImageFilter, self).__init__()

        self.name = name  # 'unsharp'
        self.settings = settings  # '{"value": "5:5:0.5:3:3:0.0"}'

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageFilter
        return cls(data['name'], data['settings'])

    def serialize(self):
        # type: () -> dict
        return {
            'name': self.name,
            'settings': self.settings
        }
