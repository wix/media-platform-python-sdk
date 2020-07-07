from __future__ import annotations

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest


class FileRequest(MediaPlatformRequest):
    path: str

    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super(FileRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/files', FileDescriptor)

    def set_path(self, path: str) -> FileRequest:
        self.path = path
        return self

    def _params(self) -> dict:
        return {
            'path': self.path
        }
