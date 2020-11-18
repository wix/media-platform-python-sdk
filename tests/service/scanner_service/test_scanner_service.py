import json
import unittest

import httpretty

from hamcrest import assert_that, instance_of, is_

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from media_platform.job.scan_file_job import ScanFileJob
from media_platform.service.scanner_service.scanner_service import ScannerService


class TestScannerService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    scanner_service = ScannerService('fish.appspot.com', authenticated_http_client)

    file_path = '/test_file.txt'

    @httpretty.activate
    def test_scan_file_request(self):
        self._register_scan_file_request()

        job = self.scanner_service.scan_file_request().set_source(
            Source(self.file_path)
        ).execute()

        assert_that(job, instance_of(ScanFileJob))
        assert_that(job.group_id, is_('g'))
        assert_that(job.status, is_('pending'))
        assert_that(job.serialize()['sources'][0]['path'], is_(self.file_path))

    def _register_scan_file_request(self):
        payload = {
            'type': 'urn:job:av-scanner.scan',
            'id': 'g_1',
            'groupId': 'g',
            'status': 'pending',
            'issuer': 'urn:app:app-id',
            'sources': [
                {'path': self.file_path}
            ],
            'specification': {},
            'callback': {},
            'dateUpdated': '2017-05-22T07:17:44Z',
            'dateCreated': '2017-05-22T07:17:44Z'
        }
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(httpretty.POST, 'https://fish.appspot.com/_api/security/av/scan',
                               json.dumps(response.serialize()))
