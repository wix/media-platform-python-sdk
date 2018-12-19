from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_service.replace_extra_metadata_request import ReplaceExtraMetadataRequest
from media_platform.service.media_platform_service import MediaPlatformService


class AudioService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(AudioService, self).__init__(domain, authenticated_http_client)

    def replace_extra_metadata_request(self):
        # type: () -> ReplaceExtraMetadataRequest
        return ReplaceExtraMetadataRequest(self._authenticated_http_client, self._base_url)
