from __future__ import annotations

from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, ACL
from media_platform.service.media_platform_request import MediaPlatformRequest


class UpdateFileRequest(MediaPlatformRequest):
    file_id = None
    path = None
    acl = None

    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super(UpdateFileRequest, self).__init__(authenticated_http_client, 'PUT', base_url + '/files', FileDescriptor)

    def set_path(self, path: str) -> UpdateFileRequest:
        self.path = path
        return self

    def set_id(self, file_id: str) -> UpdateFileRequest:
        self.file_id = file_id
        return self

    def set_acl(self, acl: ACL) -> UpdateFileRequest:
        self.acl = acl
        return self

    def execute(self) -> FileDescriptor:
        return super(UpdateFileRequest, self).execute()

    def validate(self):
        FileDescriptor.acl_validator(self.acl)

        if self.path is not None:
            FileDescriptor.path_validator(self.path)

        if not self.path and not self.file_id:
            raise ValueError('must provide path or id')

    def _params(self) -> dict:
        return {
            'id': self.file_id,
            'path': self.path,
            'acl': self.acl,
        }
