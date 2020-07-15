from __future__ import annotations

from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class SubsetFontResult(JobResult):
    type = JobType.subset_font

    def __init__(self, code: int = None, message: str = None, file_descriptor: FileDescriptor = None):
        super(SubsetFontResult, self).__init__(code, message)
        self.file_descriptor = file_descriptor

    @classmethod
    def deserialize(cls, data: dict or None) -> SubsetFontResult or None:
        if data is None:
            return None

        result = JobResult.deserialize(data)
        result.__class__ = SubsetFontResult

        payload_data = data.get('payload')
        result.file_descriptor = FileDescriptor.deserialize(payload_data) if payload_data else None
        return result

    def serialize(self) -> dict:
        data = super(SubsetFontResult, self).serialize()
        data['payload'] = self.file_descriptor.serialize() if self.file_descriptor else None

        return data
