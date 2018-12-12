from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class FileUploadCallbackPayload(Deserializable):
    def __init__(self, file_descriptor, attachment=None):
        # type: (FileDescriptor, dict or None) -> None
        self.file_descriptor = file_descriptor
        self.attachment = attachment

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FileUploadCallbackPayload
        return cls(FileDescriptor.deserialize(data['file']), data.get('attachment'))
