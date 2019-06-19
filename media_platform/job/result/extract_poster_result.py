from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractPosterResult(JobResult):
    type = JobType.extract_poster

    def __init__(self, code=None, message=None, file_descriptor=None):
        # type: (int, str, FileDescriptor) -> None
        super(ExtractPosterResult, self).__init__(code, message)
        self.payload = file_descriptor

    @classmethod
    def deserialize(cls, data):
        if data is None:
            return None

        payload_data = data.get('payload')
        result = JobResult.deserialize(data)
        result.payload = FileDescriptor.deserialize(payload_data) if payload_data else None
        result.__class__ = ExtractPosterResult
        return result

    def serialize(self):
        data = super(ExtractPosterResult, self).serialize()
        data['payload'] = self.payload.serialize() if self.payload else None

        return data
