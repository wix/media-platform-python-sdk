from __future__ import annotations

from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class MediaType:
    undefined = ''
    image = 'image'
    video = 'video'
    audio = 'audio'
    font = 'font'


class FileMetadata(Deserializable):
    def __init__(self, media_type: str, file_descriptor: FileDescriptor, basic: Deserializable = None):
        self.media_type = media_type
        self.file_descriptor = file_descriptor
        self.basic = basic

    @classmethod
    def deserialize(cls, data: dict) -> FileMetadata:
        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])

        return FileMetadata(MediaType.undefined, file_descriptor)
