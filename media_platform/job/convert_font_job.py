from __future__ import annotations

from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


class FontType:
    woff = 'woff'
    woff2 = 'woff2'
    ttf = 'ttf'
    otf = 'otf'

    values = [woff, woff2, ttf, otf]

    @classmethod
    def has_value(cls, value: FontType or str) -> bool:
        return value in cls.values


class FontSet:
    web = 'web'

    values = [web]

    @classmethod
    def has_value(cls, value: FontSet or str) -> bool:
        return value in cls.values


class ConvertFontSpecification(Specification):
    def __init__(self, destination: Destination, font_type: FontType = None, font_set: FontSet = None):
        self.destination = destination

        self.font_type = font_type
        self.font_set = font_set

    @classmethod
    def deserialize(cls, data: dict) -> ConvertFontSpecification:
        destination = Destination.deserialize(data['destination'])

        return ConvertFontSpecification(destination, data.get('fontType'), data.get('fontSet'))

    def serialize(self) -> dict:
        return {
            'destination': self.destination.serialize(),
            'fontType': self.font_type,
            'fontSet': self.font_set
        }

    def validate(self):
        if not self.font_type and not self.font_set:
            raise ValueError('must select type or set')

        if self.font_set and not self.destination.directory:
            raise ValueError('must provide destination directory for font set')

        if self.font_type:
            self._validate_font_type(self.font_type)

        if self.font_set:
            self._validate_font_set(self.font_set)

    @staticmethod
    def _validate_font_type(font_type: FontType or str):
        if not FontType.has_value(font_type):
            raise ValueError('font format must be one of: %s' % ', '.join(FontType.values))

    @staticmethod
    def _validate_font_set(font_set: FontSet or str):
        if not FontSet.has_value(font_set):
            raise ValueError('font ste must be one of: %s' % ', '.join(FontSet.values))


class ConvertFontJob(Job):
    type = JobType.convert_font
    specification_type = ConvertFontSpecification
