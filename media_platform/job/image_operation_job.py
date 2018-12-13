from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.job.job import Job
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class ImageOperationSpecification(Specification):
    def __init__(self, command, destination):
        # type: (str, Destination) -> None
        super(ImageOperationSpecification, self).__init__()

        self.command = command
        self.destination = destination

    def serialize(self):
        # type: () -> dict
        return {
            'command': self.command,
            'destination': self.destination.serialize()
        }

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageOperationSpecification
        destination = Destination.deserialize(data['destination'])

        return ImageOperationSpecification(data['command'], destination)


class ImageOperationJob(Job):

    type = 'urn:job:image.operation'

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(ImageOperationJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                            callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageOperationJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = ImageOperationSpecification.deserialize(data['specification'])
        if data.get('result'):
            # todo: result payload is FileDescriptor
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
