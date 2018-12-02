import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, FileType
from media_platform.service.file_service.file_service import FileService
from media_platform.service.rest_result import RestResult


class TestFileService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    file_service = FileService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_get_file_request(self):
        payload = FileDescriptor('/fish.txt', 'file-id', FileType.file, 'txt/plain', 123).serialize()
        response_body = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/files?path=%2Ffist.txt',
            body=json.dumps(response_body.serialize())
        )

        file_descriptor = self.file_service.get_file_request().set_path('/fish.txt').execute()

        assert_that(file_descriptor.serialize(), is_(payload))
        assert_that(file_descriptor, instance_of(FileDescriptor))
        assert_that(httpretty.last_request().querystring, is_({
            'path': ['/fish.txt']
        }))

    @httpretty.activate
    def test_get_create_request(self):
        payload = FileDescriptor('/fish.txt', 'file-id', FileType.file, 'txt/plain', 123).serialize()
        response_body = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/files',
            body=json.dumps(response_body.serialize())
        )

        file_descriptor = self.file_service.create_file_request().set_path('/fish.txt').execute()

        assert_that(file_descriptor.serialize(), is_(payload))
        assert_that(file_descriptor, instance_of(FileDescriptor))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'mimeType': 'application/vnd.wix-media.dir',
                        'path': '/fish.txt',
                        'size': 0,
                        'type': 'd',
                        'acl': 'public'
                    }))
