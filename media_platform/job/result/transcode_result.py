from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class TranscodeResult(JobResult):
    type = JobType.transcode

    def __init__(self, code=None, message=None, file_descriptor=None, master_ffmpeg_command=None):
        super(TranscodeResult, self).__init__(code, message)
        self.file_descriptor = file_descriptor
        self.master_ffmpeg_command = master_ffmpeg_command

    @classmethod
    def deserialize(cls, data):
        # type: (dict or None) -> TranscodeResult or None
        if data is None:
            return None

        result = JobResult.deserialize(data)
        result.file_descriptor = None
        result.master_ffmpeg_command = None

        payload_data = data.get('payload')
        if payload_data:
            # todo: payload.file is deprecated
            file_descriptor_data = payload_data.get('file')
            if file_descriptor_data:
                result.file_descriptor = FileDescriptor.deserialize(file_descriptor_data)

            result.master_ffmpeg_command = payload_data.get('masterFFMpegCommand')

        result.__class__ = TranscodeResult
        return result

    def serialize(self):
        # type: () -> dict
        data = super(TranscodeResult, self).serialize()
        data['payload'] = self._serialize_payload()

        return data

    def _serialize_payload(self):
        payload = None

        if self.file_descriptor:
            payload = self.file_descriptor.serialize()
            # backwards compatibility
            payload['file'] = self.file_descriptor.serialize()

        if self.master_ffmpeg_command:
            if not payload:
                payload = {}

            payload['masterFFMpegCommand'] = self.master_ffmpeg_command

        return payload

