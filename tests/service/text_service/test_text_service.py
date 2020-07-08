import json
import unittest

import httpretty
from hamcrest import assert_that, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.convert_font_job import ConvertFontSpecification, FontType
from media_platform.job.subset_font_job import SubsetFontSpecification
from media_platform.service.destination import Destination
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from media_platform.service.text_service.text_service import TextService


class TestTextService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    text_service = TextService('fish.appspot.com', authenticated_http_client)

    @httpretty.activate
    def test_convert_font_request(self):
        payload = {
            'groupId': 'g',
            'jobs': [{
                'type': 'urn:job:text.font.convert',
                'id': 'g_1',
                'groupId': 'g',
                'status': 'pending',
                'issuer': 'urn:app:app-id',
                'sources': [
                    {'path': '/font.ttf'}
                ],
                'specification': {
                    'destination': {
                        'path': '/font.woff',
                        'acl': 'public'
                    },
                    'fontType': 'woff'
                },
                'callback': None,
                'dateUpdated': '2017-05-22T07:17:44Z',
                'dateCreated': '2017-05-22T07:17:44Z'
            }]
        }

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/fonts/convert',
            body=json.dumps(response.serialize())
        )

        job_group = self.text_service.convert_font_request().set_source(
            Source('/font.ttf')
        ).set_specification(
            ConvertFontSpecification(
                Destination('/font.woff'),
                FontType.woff
            )
        ).execute()

        assert_that(job_group.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'source': {
                            'path': '/font.ttf',
                            'fileId': None
                        },
                        'specification': {
                            'destination': {
                                'directory': None,
                                'path': '/font.woff',
                                'bucket': None,
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'fontSet': None,
                            'fontType': 'woff'
                        },
                        'jobCallback': None
                    }))

    @httpretty.activate
    def test_subset_font_request(self):
        payload = {
            'groupId': 'g',
            'jobs': [{
                'type': 'urn:job:text.font.subset',
                'id': 'g_1',
                'groupId': 'g',
                'status': 'pending',
                'issuer': 'urn:app:app-id',
                'sources': [
                    {'path': '/font.ttf'}
                ],
                'specification': {
                    'destination': {
                        'path': '/font.en.ttf',
                        'acl': 'public'
                    },
                    'languageCode': 'en'
                },
                'callback': {
                    'url': 'https://i.will.be.back/'
                },
                'dateUpdated': '2017-05-22T07:17:44Z',
                'dateCreated': '2017-05-22T07:17:44Z'
            }]
        }

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/fonts/subset',
            body=json.dumps(response.serialize())
        )

        job_group = self.text_service.subset_font_request().set_source(
            Source('/font.ttf')
        ).set_specification(
            SubsetFontSpecification(
                Destination('/font.en.ttf'),
                'en'
            )
        ).execute()

        assert_that(job_group.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'source': {
                            'path': '/font.ttf',
                            'fileId': None
                        },
                        'specification': {
                            'destination': {
                                'directory': None,
                                'path': '/font.en.ttf',
                                'bucket': None,
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'languageCode': 'en'
                        },
                        'jobCallback': None
                    }))
