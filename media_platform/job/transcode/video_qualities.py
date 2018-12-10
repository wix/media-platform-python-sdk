from media_platform.job.specification import Specification


class VideoQuality(object):
    res_2160p = '2160p'
    res_1440p = '1440p'
    res_1080p = '1080p'
    res_720p = '720p'
    res_480p = '480p'
    res_360p = '360p'
    res_240p = '240p'
    res_144p = '144p'

    # order matters!
    values = [res_144p, res_240p, res_360p, res_480p, res_720p, res_1080p, res_1440p, res_2160p]

    @classmethod
    def has_value(cls, value):
        # type: (str) -> bool
        return value in cls.values


class VideoQualityRange(Specification):
    def __init__(self, minimum, maximum):
        # type: (str, str) -> None

        self.minimum = minimum
        self.maximum = maximum

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> VideoQualityRange
        return VideoQualityRange(data['minimum'], data['maximum'])

    def serialize(self):
        # type: () -> dict
        return {
            'minimum': self.minimum,
            'maximum': self.maximum
        }

    def validate(self):
        if not (self.maximum and self.minimum):
            raise ValueError('must define minimum and maximum')

        if not VideoQuality.has_value(self.minimum):
            raise ValueError('minimum value %s not supported' % self.minimum)

        if not VideoQuality.has_value(self.maximum):
            raise ValueError('maximum value %s not supported' % self.maximum)

        if VideoQuality.values.index(self.maximum) < VideoQuality.values.index(self.minimum):
            raise ValueError('maximum %s is greater than minimum %s' % (self.maximum, self.minimum))
