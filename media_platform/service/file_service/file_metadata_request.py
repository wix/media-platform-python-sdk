from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.file_metadata import FileMetadata
from media_platform.service.media_platform_request import MediaPlatformRequest
# noinspection PyProtectedMember
from media_platform.metadata.file_metadata_deserializer import _FileMetadataDeserializer


class FileMetadataRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'GET', base_url + '/files/metadata', _FileMetadataDeserializer)
        self.path = None

    def set_path(self, path: str) -> FileMetadataRequest:
        self.path = path
        return self

    def execute(self) -> FileMetadata:
        return super().execute()

    def _params(self) -> dict:
        return {
            'path': self.path
        }
