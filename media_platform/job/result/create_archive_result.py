from __future__ import annotations

from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class CreateArchiveResult(JobResult):
    type = JobType.create_archive

    def __init__(self, code: int = None, message: str = None, file_descriptor: FileDescriptor = None):
        super().__init__(code, message)
        self.file_descriptor = file_descriptor

    @classmethod
    def deserialize(cls, data: dict or None) -> CreateArchiveResult or None:
        if not data:
            return None

        payload = data.get('payload')
        result = JobResult.deserialize(data)
        result.__class__ = CreateArchiveResult
        result.file_descriptor = FileDescriptor.deserialize(payload) if payload else None
        return result

    def serialize(self) -> dict:
        data = super().serialize()
        data['payload'] = self.file_descriptor.serialize() if self.file_descriptor else None
        return data
