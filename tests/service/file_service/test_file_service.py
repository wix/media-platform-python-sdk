import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, FileType, FileMimeType, ACL
from media_platform.service.file_service.file_service import FileService
from media_platform.service.file_service.upload_url import UploadUrl
from media_platform.service.rest_result import RestResult


class TestFileService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    file_service = FileService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_get_file_request(self):
        payload = FileDescriptor('/fish.txt', 'file-id', FileType.file, 'text/plain', 123).serialize()
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
    def test_create_file_request(self):
        payload = FileDescriptor('/fish', 'file-id', FileType.directory, FileMimeType.directory, 0).serialize()
        response_body = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/files',
            body=json.dumps(response_body.serialize())
        )

        file_descriptor = self.file_service.create_file_request().set_path('/fish').execute()

        assert_that(file_descriptor.serialize(), is_(payload))
        assert_that(file_descriptor, instance_of(FileDescriptor))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'mimeType': FileMimeType.directory,
                        'path': '/fish',
                        'size': 0,
                        'type': FileType.directory,
                        'acl': ACL.public
                    }))

    @httpretty.activate
    def test_upload_url_request(self):
        response_body = RestResult(0, 'OK', {
            'uploadToken': 'token',
            'uploadUrl': 'url'
        })
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/upload/url',
            body=json.dumps(response_body.serialize())
        )

        upload_url = self.file_service.upload_url_request().set_path('/fish.txt').execute()

        assert_that(upload_url, instance_of(UploadUrl))
        assert_that(upload_url.upload_token, is_('token'))
        assert_that(upload_url.upload_url, is_('url'))
        assert_that(httpretty.last_request().querystring), is_({
            'path': '/fish.txt',
            'acl': 'public',
            'mimeType': 'application/octet-stream',
        })

    @httpretty.activate
    def test_upload_file_request(self):
        url_response_body = RestResult(0, 'OK', {
            'uploadToken': 'token',
            'uploadUrl': 'https://fish.barrel/cryptic-path'
        })
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/upload/url',
            body=json.dumps(url_response_body.serialize())
        )

        upload_response_body = RestResult(0, 'OK', [
            FileDescriptor('/fish.txt', 'file-id', FileType.file, 'text/plain', 123).serialize()
        ])
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/cryptic-path',
            body=json.dumps(upload_response_body.serialize())
        )

        file_descriptor = self.file_service.upload_file_request().set_acl(ACL.private).set_path('/fish.txt').execute()

        assert_that(file_descriptor, instance_of(FileDescriptor))
        assert_that(file_descriptor.path, is_('/fish.txt'))
