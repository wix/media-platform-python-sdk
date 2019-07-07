from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractStoryboardResult(JobResult):
    type = JobType.extract_storyboard

    def __init__(self, code=None, message=None, file_descriptors=None):
        # type: (int, str, [FileDescriptor]) -> None
        super(ExtractStoryboardResult, self).__init__(code, message)

        self.payload = file_descriptors or []

    @classmethod
    def deserialize(cls, data):
        if data is None:
            return None

        result = JobResult.deserialize(data)
        payload_data = data.get('payload') or []
        result.payload = [FileDescriptor.deserialize(d) for d in payload_data]
        result.__class__ = ExtractStoryboardResult

        return result

    def serialize(self):
        data = super(ExtractStoryboardResult, self).serialize()
        data['payload'] = [f.serialize() for f in self.payload]

        return data
