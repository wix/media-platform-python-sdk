from __future__ import annotations

from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractStoryboardResult(JobResult):
    type = JobType.extract_storyboard

    def __init__(self, code: int = None, message: str = None, file_descriptors: [FileDescriptor] = None):
        super().__init__(code, message)
        self.file_descriptors = file_descriptors or []

    @classmethod
    def deserialize(cls, data: dict or None) -> ExtractStoryboardResult or None:
        if data is None:
            return None

        result = JobResult.deserialize(data)
        result.__class__ = ExtractStoryboardResult

        payload_data = data.get('payload') or []
        result.file_descriptors = [FileDescriptor.deserialize(d) for d in payload_data]

        return result

    def serialize(self) -> dict:
        data = super().serialize()
        data['payload'] = [f.serialize() for f in self.file_descriptors]

        return data
