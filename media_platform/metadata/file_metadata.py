from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class MediaType(object):
    undefined = ''
    image = 'image'
    video = 'video'
    audio = 'audio'
    font = 'font'


class FileMetadata(Deserializable):
    def __init__(self, media_type, file_descriptor, basic=None):
        # type: (str, FileDescriptor, Deserializable) -> None
        super(FileMetadata, self).__init__()

        self.media_type = media_type
        self.file_descriptor = file_descriptor
        self.basic = basic

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FileMetadata
        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])

        return FileMetadata(MediaType.undefined, file_descriptor)
