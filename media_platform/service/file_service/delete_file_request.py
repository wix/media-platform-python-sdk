from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest


class DeleteFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(DeleteFileRequest, self).__init__(authenticated_http_client, 'DELETE', base_url + '/files', None)

        self.path = None

    def set_path(self, path):
        # type: (str) -> DeleteFileRequest
        self.path = path
        return self

    def execute(self):
        # type: () -> None
        return super(DeleteFileRequest, self).execute()

    def validate(self):
        FileDescriptor.path_validator(self.path)

    def _params(self):
        return {
            'path': self.path
        }
