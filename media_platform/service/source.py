from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class Source(Serializable, Deserializable):
    def __init__(self, path: str = None, file_id: str = None):
        self._validate(path, file_id)
        self.path = path
        self.file_id = file_id

    @classmethod
    def deserialize(cls, data: dict) -> Source:
        return Source(data.get('path'), data.get('fileId'))

    def serialize(self) -> dict:
        return {
            'path': self.path,
            'fileId': self.file_id
        }

    @staticmethod
    def _validate(path: str, file_id: str):
        if not (path or file_id):
            raise ValueError('path or file id must be specified')

        if path:
            FileDescriptor.path_validator(path)
