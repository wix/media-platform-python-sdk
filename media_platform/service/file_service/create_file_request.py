from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, FileMimeType, FileType, ACL
from media_platform.service.media_platform_request import MediaPlatformRequest


class CreateFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/files', FileDescriptor)
        self.path: str or None = None
        self.mime_type: FileMimeType = FileMimeType.directory
        self.type: FileType = FileType.directory
        self.acl: ACL = ACL.public
        self.size: int = 0
        self.file_id: str or None = None
        self.bucket: str or None = None

    def set_path(self, path: str) -> CreateFileRequest:
        self.path = path
        return self

    def set_mime_type(self, mime_type: FileMimeType) -> CreateFileRequest:
        self.mime_type = mime_type
        return self

    def set_type(self, file_type: FileType) -> CreateFileRequest:
        self.type = file_type
        return self

    def set_acl(self, acl: ACL) -> CreateFileRequest:
        self.acl = acl
        return self

    def set_size(self, size: int) -> CreateFileRequest:
        self.size = size
        return self

    def set_id(self, file_id: str) -> CreateFileRequest:
        self.file_id = file_id
        return self

    def set_bucket(self, bucket: str) -> CreateFileRequest:
        self.bucket = bucket
        return self

    def _params(self) -> dict:
        return {
            'path': self.path,
            'mimeType': self.mime_type,
            'type': self.type,
            'acl': self.acl,
            'size': self.size,
            'id': self.file_id,
            'bucket': self.bucket
        }
