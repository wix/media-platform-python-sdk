from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_service import MediaPlatformService
from media_platform.service.transcode_service.playlist_request import PlaylistRequest
from media_platform.service.transcode_service.transcode_request import TranscodeRequest


class TranscodeService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(TranscodeService, self).__init__(domain, authenticated_http_client)

    def transcode_request(self):
        # type: () -> TranscodeRequest
        return TranscodeRequest(self._authenticated_http_client, self._base_url)

    def playlist_request(self):
        # type: () -> PlaylistRequest
        return PlaylistRequest(self._domain)

    # todo: packager ?
