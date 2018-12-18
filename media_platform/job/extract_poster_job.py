from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


# todo: proper class
SUPPORTED_IMAGE_FORMATS = ['jpg', 'png']


class ExtractPosterSpecification(Specification):
    def __init__(self, second, destination, image_format='jpg'):
        # type: (float, Destination, str) -> None
        super(ExtractPosterSpecification, self).__init__()

        self.second = second
        self.destination = destination
        self.image_format = image_format or 'jpg'

    def serialize(self):
        # type: () -> dict
        return {
            'second': self.second,
            'destination': self.destination.serialize(),
            'format': self.image_format
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractPosterSpecification
        destination = Destination.deserialize(data['destination'])

        return ExtractPosterSpecification(data['second'], destination, data['format'])

    def validate(self):
        if self.image_format not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError('image format must be one of: %s' % ', '.join(SUPPORTED_IMAGE_FORMATS))


class ExtractPosterJob(Job):
    type = 'urn:job:av.poster'
    specification_type = ExtractPosterSpecification
