from __future__ import annotations

from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class _CreateFilesResponse(Deserializable):
    def __init__(self, file_descriptors: [FileDescriptor]):
        self.file_descriptors = file_descriptors

    @classmethod
    def deserialize(cls, data: dict) -> _CreateFilesResponse:
        return cls([FileDescriptor.deserialize(f) for f in data['files']])
