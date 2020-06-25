from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.live_service.close_stream_request import CloseStreamRequest
from media_platform.service.live_service.live_stream import LiveStream
from media_platform.service.live_service.open_stream_request import OpenStreamRequest
from media_platform.service.media_platform_request import MediaPlatformRequest
from media_platform.service.media_platform_service import MediaPlatformService


class GetStreamRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(GetStreamRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/live/stream/', LiveStream)

        self.id = None

        self._url = base_url + '/live/stream/'

    def set_id(self, stream_id):
        # type: (str) -> GetStreamRequest
        self.id = stream_id
        return self

    def execute(self):
        # type: () -> LiveStream

        self.url = self._url + self.id

        return super(GetStreamRequest, self).execute()


class LiveService(MediaPlatformService):
    def open_stream_request(self):
        # type: () -> OpenStreamRequest
        return OpenStreamRequest(self._authenticated_http_client, self._base_url)

    def close_stream_request(self):
        # type: () -> CloseStreamRequest
        return CloseStreamRequest(self._authenticated_http_client, self._base_url)

    def get_stream_request(self):
        return GetStreamRequest(self._authenticated_http_client, self._base_url)