from __future__ import annotations

from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.job.job import Job


class ImageOperationSpecification(Specification):
    def __init__(self, command: str, destination: Destination):
        self.command = command
        self.destination = destination

    def serialize(self) -> dict:
        return {
            'command': self.command,
            'destination': self.destination.serialize()
        }

    @classmethod
    def deserialize(cls, data: dict) -> ImageOperationSpecification:
        destination = Destination.deserialize(data['destination'])

        return ImageOperationSpecification(data['command'], destination)


class ImageOperationJob(Job):
    type = JobType.image_operation
    specification_type = ImageOperationSpecification
