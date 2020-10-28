from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.source import Source


class CopyFileRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'POST', base_url + '/copy/file', FileDescriptor)
        self.source = None
        self.destination = None

    def set_source(self, source: Source) -> CopyFileRequest:
        self.source = source
        return self

    def set_destination(self, destination: Destination) -> CopyFileRequest:
        self.destination = destination
        return self

    def _params(self) -> dict:
        return {
            'source': self.source.serialize(),
            'destination': self.destination.serialize(),
        }
