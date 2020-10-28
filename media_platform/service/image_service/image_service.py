from __future__ import annotations

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.image_service.extract_features_request import ExtractFeaturesRequest
from media_platform.service.image_service.image_operation_request import ImageOperationRequest
from media_platform.service.image_service.image_token import ImageToken, Policy, Watermark
from media_platform.service.media_platform_service import MediaPlatformService


class ImageService(MediaPlatformService):
    def __init__(self, domain: str, authenticated_http_client: AuthenticatedHTTPClient,
                 app_authenticator: AppAuthenticator):
        super().__init__(domain, authenticated_http_client)
        self.app_authenticator = app_authenticator

    def extract_features_request(self) -> ExtractFeaturesRequest:
        return ExtractFeaturesRequest(self._authenticated_http_client, self._base_url)

    def image_operation_request(self) -> ImageOperationRequest:
        return ImageOperationRequest(self._authenticated_http_client, self._base_url)

    def token(self, policy: Policy = None, watermark: Watermark = None) -> ImageToken:
        token = self.app_authenticator.default_token()

        image_token = ImageToken.from_token(token)
        image_token.policy = policy
        image_token.watermark = watermark

        return image_token

    def sign_token(self, token: ImageToken) -> str:
        return self.app_authenticator.sign_token(token)
