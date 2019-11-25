from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, ACL
from media_platform.service.media_platform_request import MediaPlatformRequest


class UpdateFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(UpdateFileRequest, self).__init__(authenticated_http_client, 'PUT', base_url + '/files', FileDescriptor)

        self.file_id = None
        self.path = None
        self.acl = None

    def set_path(self, path):
        # type: (str) -> UpdateFileRequest
        self.path = path
        return self

    def set_id(self, file_id):
        # type: (str) -> UpdateFileRequest
        self.file_id = file_id
        return self

    def set_acl(self, acl):
        # type: (ACL) -> UpdateFileRequest
        self.acl = acl
        return self

    def execute(self):
        # type: () -> FileDescriptor
        return super(UpdateFileRequest, self).execute()

    def validate(self):
        FileDescriptor.acl_validator(self.acl)

        if self.path is not None:
            FileDescriptor.path_validator(self.path)

        if not self.path and not self.file_id:
            raise ValueError('must provide path or id')

    def _params(self):
        return {
            'id': self.file_id,
            'path': self.path,
            'acl': self.acl,
        }
