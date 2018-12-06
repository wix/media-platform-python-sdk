from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_service import MediaPlatformService
from media_platform.service.video_service.extract_poster_request import ExtractPosterRequest
from media_platform.service.video_service.extract_storyboard_request import ExtractStoryboardRequest


class VideoService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(VideoService, self).__init__(domain, authenticated_http_client)

    def extract_poster_request(self):
        # type: () -> ExtractPosterRequest
        return ExtractPosterRequest(self._authenticated_http_client, self._base_url)

    def extract_storyboard_request(self):
        # type: () -> ExtractStoryboardRequest
        return ExtractStoryboardRequest(self._authenticated_http_client, self._base_url)
