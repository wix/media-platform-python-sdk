from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest


class FileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(FileRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/files', FileDescriptor)

        self.path = None

    def set_path(self, path):
        # type: (str) -> FileRequest
        self.path = path
        return self

    def _params(self):
        # type: () -> dict
        return {
            'path': self.path
        }
