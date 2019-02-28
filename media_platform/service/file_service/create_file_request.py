from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, FileMimeType, FileType, ACL
from media_platform.service.media_platform_request import MediaPlatformRequest


class CreateFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(CreateFileRequest, self).__init__(authenticated_http_client, 'POST', base_url + '/files', FileDescriptor)

        self.path = None
        self.mime_type = FileMimeType.directory
        self.type = FileType.directory
        self.acl = ACL.public
        self.size = 0
        self.id = None
        self.bucket = None

    def set_path(self, path):
        # type: (str) -> CreateFileRequest
        self.path = path
        return self

    def set_mime_type(self, mime_type):
        # type: (FileMimeType) -> CreateFileRequest
        self.mime_type = mime_type
        return self

    def set_type(self, file_type):
        # type: (FileType) -> CreateFileRequest
        self.type = file_type
        return self

    def set_acl(self, acl):
        # type: (ACL) -> CreateFileRequest
        self.acl = acl
        return self

    def set_size(self, size):
        # type: (int) -> CreateFileRequest
        self.size = size
        return self

    def set_id(self, id):
        # type: (str) -> CreateFileRequest
        self.id = id
        return self

    def set_bucket(self, bucket):
        # type: (str) -> CreateFileRequest
        self.bucket = bucket
        return self

    def _params(self):
        return {
            'path': self.path,
            'mimeType': self.mime_type,
            'type': self.type,
            'acl': self.acl,
            'size': self.size,
            'id': self.id,
            'bucket': self.bucket
        }
