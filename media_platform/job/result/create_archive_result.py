from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class CreateArchiveResult(JobResult):
    type = JobType.create_archive

    def __init__(self, code=None, message=None, created_file_descriptor=None):
        # type: (int, str, FileDescriptor) -> None
        super(CreateArchiveResult, self).__init__(code, message)
        self.created_file_descriptor = created_file_descriptor

    @classmethod
    def deserialize(cls, data):
        # type: (dict or None) -> CreateArchiveResult or None
        if not data:
            return None

        payload = data.get('payload')
        result = JobResult.deserialize(data)
        result.created_file_descriptor = FileDescriptor.deserialize(payload) if payload else None
        result.__class__ = CreateArchiveResult
        return result

    def serialize(self):
        # type: () -> dict
        data = super(CreateArchiveResult, self).serialize()
        data['payload'] = self.created_file_descriptor.serialize() if self.created_file_descriptor else None
        return data


