import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_, equal_to, not_none
from requests.exceptions import RetryError

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.exception.conflict_exception import ConflictException
from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.rest_result import RestResult
from tests.http_client.dummy_payload import DummyPayload


class TestAuthenticatedHTTPClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_authenticator = AppAuthenticator('app-id', '95eee2c63ac2d15270628664c84f6ddd')
        cls.authenticated_http_client = AuthenticatedHTTPClient(cls.app_authenticator)
        cls.test_endpoint = 'https://fish.barrel/get'

    @httpretty.activate
    def test_get(self):
        payload = DummyPayload('fish')
        response_body = RestResult(0, 'OK', payload.serialize())

        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            body=json.dumps(response_body.serialize())
        )

        payload = self.authenticated_http_client.get(self.test_endpoint, payload_type=DummyPayload)

        assert_that(payload, instance_of(DummyPayload))
        assert_that(payload.dumdum, is_('fish'))
        assert_that(httpretty.last_request().headers.get('Authorization'), not_none())

    @httpretty.activate
    def test_get_unexpected_null_payload(self):
        response_body = RestResult(0, 'OK')

        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            body=json.dumps(response_body.serialize())
        )

        payload = self.authenticated_http_client.get(self.test_endpoint, payload_type=DummyPayload)
        assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_expected_null_payload(self):
        response_body = RestResult(0, 'OK')
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            body=json.dumps(response_body.serialize())
        )

        payload = self.authenticated_http_client.get(self.test_endpoint)
        assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_401(self):
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=401
        )

        with self.assertRaises(UnauthorizedException):
            self.authenticated_http_client.get(self.test_endpoint)

    @httpretty.activate
    def test_get_403(self):
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=403
        )

        with self.assertRaises(ForbiddenException):
            self.authenticated_http_client.get(self.test_endpoint)

    @httpretty.activate
    def test_get_404(self):
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=404
        )

        with self.assertRaises(NotFoundException):
            self.authenticated_http_client.get(self.test_endpoint)

    @httpretty.activate
    def test_get_409(self):
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=409
        )

        with self.assertRaises(ConflictException):
            self.authenticated_http_client.get(self.test_endpoint)

    @httpretty.activate
    def test_get_some_other_error_status(self):
        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=405
        )

        with self.assertRaises(MediaPlatformException):
            self.authenticated_http_client.get(self.test_endpoint)

    @httpretty.activate
    def test_get_500_retry(self):
        authenticated_http_client = AuthenticatedHTTPClient(self.app_authenticator, retry_count=1,
                                                            retry_backoff_factor=0)

        httpretty.register_uri(
            httpretty.GET,
            self.test_endpoint,
            status=500
        )

        with self.assertRaises(MediaPlatformException) as e:
            authenticated_http_client.get(self.test_endpoint)
            # todo: assert httpretty.latest_requests() when released

        media_platform_exception = e.exception
        assert_that(isinstance(media_platform_exception.cause, RetryError), equal_to(True))
