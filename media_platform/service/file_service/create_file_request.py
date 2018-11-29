from media_platform.service import file_descriptor
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest


class CreateFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        super(CreateFileRequest, self).__init__(authenticated_http_client, "POST", base_url + "/files", FileDescriptor)

        self.path = None
        self.mime_type = file_descriptor.FileMimeType.directory
        self.type = file_descriptor.FileType.directory
        self.acl = file_descriptor.ACL.public
        self.size = 0

    def serialize(self):
        return {
            'path': self.path,
            'mimeType': self.mime_type,
            'type': self.type,
            'acl': self.acl,
            'size': self.size
        }
