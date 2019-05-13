from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job

# todo: proper class
SUPPORTED_IMAGE_FORMATS = ['jpg', 'png']


class ExtractPosterSpecification(Specification):
    def __init__(self, second, destination, image_format='jpg', percentage=None):
        # type: (float or None, Destination, str, float or None) -> None
        super(ExtractPosterSpecification, self).__init__()

        self.second = second
        self.percentage = percentage
        self.destination = destination
        self.image_format = image_format or 'jpg'

    def serialize(self):
        # type: () -> dict
        return {
            'second': self.second,
            'percentage': self.percentage,
            'destination': self.destination.serialize(),
            'format': self.image_format
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractPosterSpecification
        destination = Destination.deserialize(data['destination'])

        return ExtractPosterSpecification(data['second'], destination, data['format'])

    def validate(self):
        self._validate_image_format()
        self._validate_time()

    def _validate_image_format(self):
        if self.image_format not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError('image format must be one of: %s' % ', '.join(SUPPORTED_IMAGE_FORMATS))

    def _validate_time(self):
        if self.second is not None:
            return

        if self.percentage is None:
            raise ValueError('must provide second or percentage')

        if self.percentage < 0 or self.percentage > 100:
            raise ValueError('percentage must be 0-100')


class ExtractPosterJob(Job):
    type = 'urn:job:av.poster'
    specification_type = ExtractPosterSpecification
