from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class _UploadFileResponse(Deserializable):
    def __init__(self, file_descriptors):
        # type: ([FileDescriptor]) -> None
        super(_UploadFileResponse, self).__init__()

        self.file_descriptors = file_descriptors

    @classmethod
    def deserialize(cls, data):
        return _UploadFileResponse(
            [FileDescriptor.deserialize(item) for item in data]
        )
