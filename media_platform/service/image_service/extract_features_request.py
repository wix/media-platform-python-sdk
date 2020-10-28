from __future__ import annotations

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.image.image_features import ImageFeatures
from media_platform.service.media_platform_request import MediaPlatformRequest


class Feature:
    faces = 'faces'
    labels = 'labels'
    colors = 'colors'
    explicit_content = 'explicit_content'
    crop_hints = 'crop_hints'

    values = [faces, labels, colors, explicit_content, crop_hints]

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls.values


class ExtractFeaturesRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'GET', base_url + '/images/features', ImageFeatures)
        self.path = None
        self.features = []

    def set_path(self, path: str) -> ExtractFeaturesRequest:
        self.path = path
        return self

    def set_features(self, features: [Feature]) -> ExtractFeaturesRequest:
        self.features = features
        return self

    def add_features(self, *features: [Feature]) -> ExtractFeaturesRequest:
        self.features.extend(features)
        return self

    def _params(self) -> dict:
        return {
            'path': self.path,
            'features': ','.join(self.features)
        }

    def execute(self) -> ImageFeatures:
        return super().execute()
