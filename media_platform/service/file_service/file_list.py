from media_platform.lang.serialization import Deserializable
from media_platform.service.file_descriptor import FileDescriptor


class FileList(Deserializable):
    def __init__(self, next_page_token, files):
        # type: (str, [FileDescriptor]) -> None
        super(FileList, self).__init__()

        self.next_page_token = next_page_token
        self.files = files

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FileList

        files = [FileDescriptor.deserialize(f) for f in data['files']]

        return FileList(data['nextPageToken'], files)
