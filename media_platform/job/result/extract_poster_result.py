from __future__ import annotations

from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractPosterResult(JobResult):
    type = JobType.extract_poster

    def __init__(self, code: int = None, message: str = None, file_descriptor: FileDescriptor = None):
        super().__init__(code, message)
        self.file_descriptor = file_descriptor

    @classmethod
    def deserialize(cls, data: dict or None) -> ExtractPosterResult or None:
        if data is None:
            return None

        payload_data = data.get('payload')
        result = JobResult.deserialize(data)
        result.file_descriptor = FileDescriptor.deserialize(payload_data) if payload_data else None
        result.__class__ = ExtractPosterResult
        return result

    def serialize(self) -> dict:
        data = super().serialize()
        data['payload'] = self.file_descriptor.serialize() if self.file_descriptor else None

        return data
