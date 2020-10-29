from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_service import MediaPlatformService
from media_platform.service.video_service.extract_poster_request import ExtractPosterRequest
from media_platform.service.video_service.extract_storyboard_request import ExtractStoryboardRequest


class VideoService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        super().__init__(domain, authenticated_http_client)

    def extract_poster_request(self) -> ExtractPosterRequest:
        return ExtractPosterRequest(self._authenticated_http_client, self._base_url)

    def extract_storyboard_request(self) -> ExtractStoryboardRequest:
        return ExtractStoryboardRequest(self._authenticated_http_client, self._base_url)
