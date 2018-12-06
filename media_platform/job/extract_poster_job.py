from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.job.job import Job
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


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

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(ExtractPosterJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                               callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractPosterJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = ExtractPosterSpecification.deserialize(data['specification'])
        if data.get('result'):
            # todo: result payload is FileDescriptor
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
