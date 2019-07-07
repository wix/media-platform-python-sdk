from typing import Optional

from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


class PosterImageFormat(object):
    jpeg = 'jpg'
    png = 'png'
    values = [jpeg, png]
    invalid_value_message = 'Image format must be one of: %s' % ', '.join(values)


class PosterFilter(object):
    transparent_crop = 'transparentCrop'
    values = [transparent_crop]
    invalid_value_message = 'Filters must be one of: %s' % ', '.join(values)


class ExtractPosterSpecification(Specification):
    def __init__(self, second, destination, image_format=PosterImageFormat.jpeg, percentage=None, filters=None):
        # type: (Optional[float], Destination, Optional[PosterImageFormat], Optional[float], Optional[PosterFilter]) -> None
        super(ExtractPosterSpecification, self).__init__()

        self.second = second
        self.destination = destination
        self.image_format = image_format or PosterImageFormat.jpeg
        self.percentage = percentage
        self.filters = filters or []

    def serialize(self):
        # type: () -> dict
        return {
            'second': self.second,
            'percentage': self.percentage,
            'destination': self.destination.serialize(),
            'format': self.image_format,
            'filters': self.filters
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractPosterSpecification
        destination = Destination.deserialize(data['destination'])

        return ExtractPosterSpecification(data['second'], destination, data['format'], data.get('percentage'),
                                          data.get('filters'))

    def validate(self):
        self._validate_image_format()
        self._validate_time()
        self._validate_filters()

    def _validate_image_format(self):
        if self.image_format not in PosterImageFormat.values:
            raise ValueError(PosterImageFormat.invalid_value_message)

    def _validate_time(self):
        if self.second is None and self.percentage is None:
            raise ValueError('Must provide either second or percentage')

        if self.percentage is not None and (self.percentage < 0 or self.percentage > 100):
            raise ValueError('Percentage must be 0-100')

    def _validate_filters(self):
        invalid_filters = [f for f in self.filters if f not in PosterFilter.values]
        if invalid_filters:
            raise ValueError(PosterFilter.invalid_value_message)


class ExtractPosterJob(Job):
    type = JobType.extract_poster
    specification_type = ExtractPosterSpecification
