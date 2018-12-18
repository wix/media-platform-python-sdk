from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.image.image_features import ImageFeatures
from media_platform.service.media_platform_request import MediaPlatformRequest


class Feature(object):
    faces = 'faces'
    labels = 'labels'
    colors = 'colors'
    explicit_content = 'explicit_content'

    values = [faces, labels, colors, explicit_content]

    @classmethod
    def has_value(cls, value):
        # type: (str) -> bool
        return value in cls.values


class ExtractFeaturesRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(ExtractFeaturesRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/images/features',
                                                     ImageFeatures)

        self.path = None
        self.features = []

    def set_path(self, path):
        # type: (str) -> ExtractFeaturesRequest
        self.path = path
        return self

    def set_features(self, features):
        # type: ([Feature]) -> ExtractFeaturesRequest
        self.features = features
        return self

    def add_features(self, *features):
        # type: ([Feature]) -> ExtractFeaturesRequest
        self.features.extend(features)
        return self

    def _params(self):
        # type: () -> dict
        return {
            'path': self.path,
            'features': ','.join(self.features)
        }

    def execute(self):
        # type: () -> ImageFeatures
        return super(ExtractFeaturesRequest, self).execute()
