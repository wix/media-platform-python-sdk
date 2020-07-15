from __future__ import annotations

from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class FileUploadCallbackPayload(Deserializable):
    def __init__(self, file_descriptor: FileDescriptor, attachment: dict = None):
        self.file_descriptor = file_descriptor
        self.attachment = attachment

    @classmethod
    def deserialize(cls, data: dict) -> FileUploadCallbackPayload:
        return cls(FileDescriptor.deserialize(data['file']), data.get('attachment'))
