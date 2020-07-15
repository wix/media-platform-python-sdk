from __future__ import annotations

from media_platform.job.specification import Specification


class VideoQuality:
    res_144p = '144p'
    res_240p = '240p'
    res_360p = '360p'
    res_480p = '480p'
    res_720p = '720p'
    res_1080p = '1080p'
    res_1440p = '1440p'
    res_2160p = '2160p'

    # order matters!
    values = [res_144p, res_240p, res_360p, res_480p, res_720p, res_1080p, res_1440p, res_2160p]

    @classmethod
    def has_value(cls, value: str or VideoQuality) -> bool:
        return value in cls.values


class VideoQualityRange(Specification):
    def __init__(self, minimum: VideoQuality, maximum: VideoQuality):
        self.minimum = minimum
        self.maximum = maximum

    @classmethod
    def deserialize(cls, data: dict) -> VideoQualityRange:
        return VideoQualityRange(data['minimum'], data['maximum'])

    def serialize(self) -> dict:
        return {
            'minimum': self.minimum,
            'maximum': self.maximum
        }

    def validate(self):
        if not (self.maximum and self.minimum):
            raise ValueError('must define minimum and maximum')

        if not VideoQuality.has_value(str(self.minimum)):
            raise ValueError('minimum value %s not supported' % self.minimum)

        if not VideoQuality.has_value(str(self.maximum)):
            raise ValueError('maximum value %s not supported' % self.maximum)

        if VideoQuality.values.index(str(self.maximum)) < VideoQuality.values.index(str(self.minimum)):
            raise ValueError('maximum %s is greater than minimum %s' % (self.maximum, self.minimum))
