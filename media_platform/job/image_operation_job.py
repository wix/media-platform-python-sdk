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
    specification_type = ImageOperationSpecification
