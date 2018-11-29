import json
import unittest

import httpretty
from mockito import mock, when, forget_invocations
from hamcrest import assert_that, instance_of, is_

from media_platform.auth.authenticator import Authenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.rest_result import RestResult
from tests.http.dummy_payload import DummyPayload


class TestAuthenticatedHTTPClient(unittest.TestCase):

    authenticator = mock(Authenticator)

    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    # def setUp(self):
    #     self.authenticator = mock(Authenticator)

    def tearDown(self):
        # unstub()
        forget_invocations()

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

    @httpretty.activate
    def test_get_null_payload(self):
        response_body = RestResult(0, 'OK')
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/get',
            body=json.dumps(response_body.serialize())
        )

        when(self.authenticator).default_signed_token().thenReturn('xxx')

        payload = self.authenticated_http_client.get('https://fish.barrel/get')

        assert_that(payload, is_(None))
