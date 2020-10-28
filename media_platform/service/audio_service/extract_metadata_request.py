from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.audio_file_metadata import AudioFileMetadata
from media_platform.service.media_platform_request import MediaPlatformRequest


class ExtractMetadataRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'GET', base_url + '/audio/metadata', AudioFileMetadata)
        self.path = None

    def set_path(self, path: str) -> ExtractMetadataRequest:
        self.path = path
        return self

    def execute(self) -> AudioFileMetadata:
        return super().execute()

    def _params(self) -> dict:
        return {
            'path': self.path
        }
