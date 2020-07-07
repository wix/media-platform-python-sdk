from __future__ import annotations

from media_platform.service.live_service.close_stream_request import CloseStreamRequest
from media_platform.service.live_service.get_stream_request import GetStreamRequest
from media_platform.service.live_service.open_stream_request import OpenStreamRequest
from media_platform.service.media_platform_service import MediaPlatformService


class LiveService(MediaPlatformService):
    def open_stream_request(self) -> OpenStreamRequest:
        return OpenStreamRequest(self._authenticated_http_client, self._base_url)

    def close_stream_request(self) -> CloseStreamRequest:
        return CloseStreamRequest(self._authenticated_http_client, self._base_url)

    def get_stream_request(self) -> GetStreamRequest:
        return GetStreamRequest(self._authenticated_http_client, self._base_url)
