import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.create_archive_job import ArchiveType, CreateArchiveJob
from media_platform.job.extract_archive_job import ExtractionReport, ExtractionReportFormat, ExtractArchiveJob
from media_platform.service.archive_service.archive_service import ArchiveService
from media_platform.service.archive_service.create_archive_manifest_request import ZipAlgorithm
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor, FileType
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class TestArchiveService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    archive_service = ArchiveService('fish.appspot.com', authenticated_http_client)

    @httpretty.activate
    def test_create_archive_request(self):
        payload = {
            'type': 'urn:job:archive.create',
            'id': 'g_1',
            'groupId': 'g',
            'status': 'pending',
            'issuer': 'urn:app:app-id',
            'sources': [
                {'path': '/video.mp4'}
            ],
            'specification': {
                'sources': [
                    {'path': '/video.mp4'}
                ],
                'destination': {
                    'path': '/video.tar',
                    'acl': 'public'
                },
                'archiveType': 'tar'
            },
            'callback': {
                'url': 'https://call.me.back/'
            },
            'dateUpdated': '2017-05-22T07:17:44Z',
            'dateCreated': '2017-05-22T07:17:44Z'
        }

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/archive/create',
            body=json.dumps(response.serialize())
        )

        job = self.archive_service.create_archive_request().add_sources(
            Source('/video.mp4')
        ).set_destination(
            Destination('/video.tar')
        ).set_archive_type(ArchiveType.tar).set_callback(
            Callback('https://call.me.back/')
        ).execute()

        assert_that(job, instance_of(CreateArchiveJob))
        assert_that(job.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'archiveType': 'tar',
                        'sources': [{
                            'path': '/video.mp4', 'fileId': None
                        }],
                        'destination': {
                            'directory': None,
                            'path': '/video.tar',
                            'lifecycle': None,
                            'acl': 'public'
                        },
                        'jobCallback': {
                            'url': 'https://call.me.back/',
                            'headers': None,
                            'attachment': None
                        }
                    }))

    @httpretty.activate
    def test_create_archive_manifest_request(self):
        payload = FileDescriptor('/m.zip', 'file-id', FileType.file, 'application/vnd.wix-media.zip', 123).serialize()
        response_body = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/archive/create/manifest',
            body=json.dumps(response_body.serialize())
        )

        file_descriptor = self.archive_service.create_archive_manifest_request().add_sources(
            Source('/video.mp4')
        ).set_destination(
            Destination('/m.zip')
        ).set_algorithm(
            ZipAlgorithm.store
        ).set_name('archive.zip').execute()

        assert_that(file_descriptor, instance_of(FileDescriptor))
        assert_that(file_descriptor.path, is_('/m.zip'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'sources': [{
                            'path': '/video.mp4',
                            'fileId': None
                        }],
                        'destination': {
                            'directory': None,
                            'path': '/m.zip',
                            'lifecycle': None,
                            'acl': 'public'
                        },
                        'name': 'archive.zip',
                        'algorithm': 'store'
                    }))

    @httpretty.activate
    def test_extract_archive_request(self):
        payload = {
            'id': 'g_1',
            'groupId': '8c9063175f214bd78f8f6391dbc49a93',
            'type': 'urn:job:archive.extract',
            'issuer': 'urn:app:app-id',
            'status': 'success',
            'sources': [
                {
                    'path': '/video.zip',
                    'fileId': 'file id'
                }
            ],
            'specification': {
                'source': {
                    'path': '/video.zip',
                    'fileId': 'file id'
                },
                'destination': {
                    'directory': '/video',
                    'path': None,
                    'acl': 'public'
                },
                'extractedFilesReport': {
                    'destination': {
                        'directory': None,
                        'path': '/video.report.json',
                        'acl': 'public'
                    },
                    'format': 'json'
                }
            },
            'result': {
                'message': 'OK',
                'code': 0,
                'payload': {
                    'reportFileDescriptor': {
                        'path': '/video.report.json',
                        'id': 'report file id',
                        'acl': 'public',
                        'mimeType': 'application/json',
                        'size': 1718,
                        'hash': None,
                        'type': '-',
                        'dateUpdated': '2017-07-30T12:46:39Z',
                        'dateCreated': '2017-07-30T12:46:39Z',
                    }
                }
            },
            'dateCreated': '2017-07-30T12:46:31Z',
            'dateUpdated': '2017-07-30T12:46:40Z',
        }

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/archive/extract',
            body=json.dumps(response.serialize())
        )

        job = self.archive_service.extract_archive_request().set_source(
            Source('/video.zip')
        ).set_destination(
            Destination(directory='/video')
        ).set_report(
            ExtractionReport(
                Destination(path='/video.report.json'),
                ExtractionReportFormat.json
            )
        ).execute()

        assert_that(job, instance_of(ExtractArchiveJob))
        assert_that(job.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'source': {
                            'path': '/video.zip',
                            'fileId': None
                        },
                        'destination': {
                            'directory': '/video',
                            'path': None,
                            'lifecycle': None,
                            'acl': 'public'
                        },
                        'extractedFilesReport': {
                            'destination': {
                                'directory': None,
                                'path': '/video.report.json',
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'format': 'json'
                        },
                        'jobCallback': None
                    }))

    def test_archive_manifest_url_request(self):
        url = self.archive_service.archive_manifest_url_request().set_path('/path/to/manifest.zip').execute()

        assert_that(url, is_('//archive-fish.wixmp.com/path/to/manifest.zip'))
