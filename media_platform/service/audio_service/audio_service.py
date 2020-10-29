from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.audio_service.extract_metadata_request import ExtractMetadataRequest
from media_platform.service.audio_service.replace_extra_metadata_request import ReplaceExtraMetadataSyncRequest, \
    ReplaceExtraMetadataAsyncRequest

from media_platform.service.media_platform_service import MediaPlatformService


class AudioService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient):
        super().__init__(domain, authenticated_http_client)

    def extract_metadata_request(self) -> ExtractMetadataRequest:
        return ExtractMetadataRequest(self._authenticated_http_client, self._base_url)

    def replace_extra_metadata_sync_request(self) -> ReplaceExtraMetadataSyncRequest:
        return ReplaceExtraMetadataSyncRequest(self._authenticated_http_client, self._base_url)

    def replace_extra_metadata_async_request(self) -> ReplaceExtraMetadataAsyncRequest:
        return ReplaceExtraMetadataAsyncRequest(self._authenticated_http_client, self._base_url)
