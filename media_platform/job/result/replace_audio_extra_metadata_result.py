from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ReplaceAudioExtraMetadataResult(JobResult):
    type = JobType.replace_extra_metadata

    def __init__(self, code=None, message=None, file_descriptor=None):
        # type: (int, str, FileDescriptor) -> None
        super(ReplaceAudioExtraMetadataResult, self).__init__(code, message)
        self.payload = file_descriptor

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ReplaceAudioExtraMetadataResult or None
        if data is None:
            return None

        payload_data = data.get('payload')
        result = JobResult.deserialize(data)
        result.payload = FileDescriptor.deserialize(payload_data) if payload_data else None
        result.__class__ = ReplaceAudioExtraMetadataResult
        return result

    def serialize(self):
        # type: () -> dict
        data = super(ReplaceAudioExtraMetadataResult, self).serialize()
        data['payload'] = self.payload.serialize() if self.payload else None

        return data
