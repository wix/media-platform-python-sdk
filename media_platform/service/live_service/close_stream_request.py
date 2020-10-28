from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_request import MediaPlatformRequest


class CloseStreamRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'DELETE', base_url + '/live/streams/', None)

        self.stream_id = None
        self._url = base_url + '/live/streams/'

    def set_stream_id(self, stream_id: str) -> CloseStreamRequest:
        self.stream_id = stream_id
        return self

    def execute(self):
        self.url = self._url + self.stream_id
        return super().execute()
