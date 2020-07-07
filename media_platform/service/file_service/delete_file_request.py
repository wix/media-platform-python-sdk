from __future__ import annotations

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest


class DeleteFileRequest(MediaPlatformRequest):
    path: str

    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super(DeleteFileRequest, self).__init__(authenticated_http_client, 'DELETE', base_url + '/files', None)

    def set_path(self, path: str) -> DeleteFileRequest:
        self.path = path
        return self

    def execute(self):
        return super(DeleteFileRequest, self).execute()

    def validate(self):
        FileDescriptor.path_validator(self.path)

    def _params(self) -> dict:
        return {
            'path': self.path
        }
