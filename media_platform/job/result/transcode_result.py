from __future__ import annotations

from typing import Optional, Dict

from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult
from media_platform.service.file_descriptor import FileDescriptor


class TranscodeResult(JobResult):
    type = JobType.transcode

    def __init__(self, code: int = None, message: str = None, file_descriptor: FileDescriptor = None,
                 master_ffmpeg_command: str = None, error_class: str = None):
        super().__init__(code, message)
        self.file_descriptor = file_descriptor
        self.master_ffmpeg_command = master_ffmpeg_command
        self.error_class = error_class

    @classmethod
    def deserialize(cls, data: Optional[Dict]) -> Optional[TranscodeResult]:
        if data is None:
            return None

        payload_data = data.get('payload') or {}
        file_descriptor_data = payload_data.get('file')
        file_descriptor = FileDescriptor.deserialize(file_descriptor_data) if file_descriptor_data else None

        return cls(data['code'], data['message'], file_descriptor, payload_data.get('masterFFMpegCommand'),
                   payload_data.get('errorClass'))

    def serialize(self) -> Dict:
        return {
            'code': self.code,
            'message': self.message,
            'payload': self._serialize_payload()
        }

    def _serialize_payload(self) -> Dict:
        payload = {}

        if self.file_descriptor:
            payload = self.file_descriptor.serialize()
            # backwards compatibility
            payload['file'] = self.file_descriptor.serialize()

        if self.master_ffmpeg_command:
            payload['masterFFMpegCommand'] = self.master_ffmpeg_command

        if self.error_class:
            payload['errorClass'] = self.error_class

        return payload or None
