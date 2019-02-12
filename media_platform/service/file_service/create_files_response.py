from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class _CreateFilesResponse(Deserializable):
    def __init__(self, file_descriptors):
        # type: ([FileDescriptor]) -> None
        super(_CreateFilesResponse, self).__init__()

        self.file_descriptors = file_descriptors

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> _CreateFilesResponse
        return cls([FileDescriptor.deserialize(f) for f in data['files']])
