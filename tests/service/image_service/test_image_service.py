import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.metadata.image.image_features import ImageFeatures
from media_platform.service.image_service.extract_features_request import Feature
from media_platform.service.image_service.image_service import ImageService
from media_platform.service.rest_result import RestResult


class TestImageService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    image_service = ImageService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_extract_features_request(self):
        payload = {
            'colors': [
                {'pixelFraction': 0.58838487, 'r': 236, 'b': 235, 'score': 0.5731545, 'g': 232},
                {'pixelFraction': 0.09195876, 'r': 155, 'b': 119, 'score': 0.16580881, 'g': 119},
            ],
            'labels': [
                {'score': 0.8536242, 'name': 'beauty'},
                {'score': 0.71902096, 'name': 'art model'}
            ],
            'explicitContent': [
                {'likelihood': 'VERY_UNLIKELY', 'name': 'violence'},
                {'likelihood': 'VERY_LIKELY', 'name': 'adult'}
            ],
            'faces': [
                {'y': 446, 'x': 1319, 'height': 670, 'width': 580}
            ]}

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/images/features',
            body=json.dumps(response.serialize())
        )

        features = self.image_service.extract_features_request().set_path(
            '/image.png'
        ).add_features(
            Feature.explicit_content, Feature.faces, Feature.colors, Feature.labels
        ).execute()

        assert_that(features, instance_of(ImageFeatures))
        assert_that(httpretty.last_request().querystring,
                    is_({
                        'path': ['/image.png'],
                        'features': ['explicit_content,faces,colors,labels']
                    }))
