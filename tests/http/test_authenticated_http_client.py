import json
import unittest

import httpretty
from mockito import mock, when, forget_invocations, unstub
from hamcrest import assert_that, instance_of, is_

from media_platform.auth.authenticator import Authenticator
from media_platform.exception.forbidden_exception import ForbiddenException
from media_platform.exception.media_platform_exception import MediaPlatformException
from media_platform.exception.not_found_exception import NotFoundException
from media_platform.exception.unauthorized_exception import UnauthorizedException
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.rest_result import RestResult
from tests.http.dummy_payload import DummyPayload


class TestAuthenticatedHTTPClient(unittest.TestCase):
    authenticator = mock(Authenticator)

    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    def tearDown(self):
        forget_invocations()

    @classmethod
    def tearDownClass(cls):
        unstub()

    @httpretty.activate
    def test_get(self):
        payload = DummyPayload('fish')
        response_body = RestResult(0, 'OK', payload.serialize())
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            body=json.dumps(response_body.serialize())
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        payload = self.authenticated_http_client.get('https://fish.barrel/get', payload_type=DummyPayload)

        assert_that(payload, instance_of(DummyPayload))
        assert_that(payload.dumdum, is_('fish'))
        assert_that(httpretty.last_request().headers.get('Authorization'), is_('xxx'))

    @httpretty.activate
    def test_get_unexpected_null_payload(self):
        response_body = RestResult(0, 'OK')
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            body=json.dumps(response_body.serialize())
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        payload = self.authenticated_http_client.get('https://fish.barrel/get', payload_type=DummyPayload)

        assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_expected_null_payload(self):
        response_body = RestResult(0, 'OK')
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            body=json.dumps(response_body.serialize())
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        payload = self.authenticated_http_client.get('https://fish.barrel/get')

        assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_401(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            status=401
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        with self.assertRaises(UnauthorizedException):
            payload = self.authenticated_http_client.get('https://fish.barrel/get')
            assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_403(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            status=403
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        with self.assertRaises(ForbiddenException):
            payload = self.authenticated_http_client.get('https://fish.barrel/get')
            assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_404(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            status=404
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        with self.assertRaises(NotFoundException):
            payload = self.authenticated_http_client.get('https://fish.barrel/get')
            assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_some_other_error_status(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            status=405
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        with self.assertRaises(MediaPlatformException):
            payload = self.authenticated_http_client.get('https://fish.barrel/get')
            assert_that(payload, is_(None))

    @httpretty.activate
    def test_get_500_retry(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            status=500
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        with self.assertRaises(MediaPlatformException):
            payload = self.authenticated_http_client.get('https://fish.barrel/get')
            assert_that(payload, is_(None))
            # todo: assert httpretty.latest_requests() when released
