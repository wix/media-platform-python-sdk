from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.image_service.extract_features_request import ExtractFeaturesRequest
from media_platform.service.image_service.image_operation_request import ImageOperationRequest
from media_platform.service.media_platform_service import MediaPlatformService


class ImageService(MediaPlatformService):
    def __init__(self, domain, authenticated_http_client):
        # type: (str, AuthenticatedHTTPClient) -> None
        super(ImageService, self).__init__(domain, authenticated_http_client)

    def extract_features_request(self):
        # type: () -> ExtractFeaturesRequest
        return ExtractFeaturesRequest(self._authenticated_http_client, self._base_url)

    def image_operation_request(self):
        # type: () -> ImageOperationRequest
        return ImageOperationRequest(self._authenticated_http_client, self._base_url)
