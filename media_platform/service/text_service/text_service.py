from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.media_platform_service import MediaPlatformService
from media_platform.service.text_service.convert_font_request import ConvertFontRequest
from media_platform.service.text_service.subset_font_request import SubsetFontRequest


class TextService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        super().__init__(domain, authenticated_http_client)

    def convert_font_request(self) -> ConvertFontRequest:
        return ConvertFontRequest(self._authenticated_http_client, self._base_url)

    def subset_font_request(self) -> SubsetFontRequest:
        return SubsetFontRequest(self._authenticated_http_client, self._base_url)
