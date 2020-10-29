from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.live_service.live_stream import LiveStream
from media_platform.service.media_platform_request import MediaPlatformRequest


class GetStreamRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'GET', base_url + '/live/stream/', LiveStream)
        self.id = None
        self._url = base_url + '/live/stream/'

    def set_id(self, stream_id: str) -> GetStreamRequest:
        self.id = stream_id
        return self

    def execute(self) -> LiveStream:
        self.url = self._url + self.id

        return super().execute()
