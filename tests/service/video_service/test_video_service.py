import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.extract_poster_job import ExtractPosterSpecification, ExtractPosterJob
from media_platform.job.extract_storyboard_job import ExtractStoryboardSpecification, ExtractStoryboardJob
from media_platform.service.destination import Destination
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from media_platform.service.video_service.video_service import VideoService


class TestVideoService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    video_service = VideoService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_extract_poster_request(self):
        payload = {
            'groupId': 'g',
            'jobs': [{
                'id': 'g_1',
                'type': 'urn:job:av.poster',
                'groupId': 'g',
                'status': 'pending',
                'specification': {
                    'second': 20,
                    'destination': {
                        'path': '/video.poster.jpg',
                        'directory': '/',
                        'acl': 'public'
                    },
                    'format': 'jpg'
                },
                'sources': [
                    {
                        'path': '/video.mp4',
                        'fileId': '123'
                    }
                ],
                'result': None,
                'issuer': 'urn:app:app-id-1',
                'dateUpdated': '2017-05-23T08:34:43Z',
                'dateCreated': '2017-05-23T08:34:43Z',
            }]}
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/av/poster',
            body=json.dumps(response.serialize())
        )

        group = self.video_service.extract_poster_request().add_sources(
            Source('/video.mp4')
        ).add_specifications(
            ExtractPosterSpecification(20, Destination('/video.poster.jpg'), 'jpg')
        ).execute()

        assert_that(group.jobs[0], instance_of(ExtractPosterJob))
        assert_that(group.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'specifications': [{
                            'second': 20,
                            'destination': {
                                'directory': None,
                                'path': '/video.poster.jpg',
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'format': 'jpg'
                        }],
                        'sources': [{
                            'path': '/video.mp4',
                            'fileId': None
                        }]
                    }))

    @httpretty.activate
    def test_extract_storyboard_request(self):
        payload = {
            'groupId': 'g',
            'jobs': [{
                'id': 'g_1',
                'type': 'urn:job:av.storyboard',
                'groupId': 'g',
                'status': 'pending',
                'specification': {
                    'columns': 5,
                    'rows': 6,
                    'destination': {
                        'path': '/video.story.jpg',
                        'directory': '/',
                        'acl': 'public'
                    },
                    'format': 'jpg'
                },
                'sources': [
                    {
                        'path': '/video.mp4',
                        'fileId': '123'
                    }
                ],
                'result': None,
                'issuer': 'urn:app:app-id-1',
                'dateUpdated': '2017-05-23T08:34:43Z',
                'dateCreated': '2017-05-23T08:34:43Z',
            }]}

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/av/storyboard',
            body=json.dumps(response.serialize())
        )

        group = self.video_service.extract_storyboard_request().add_sources(
            Source('/video.mp4')
        ).add_specifications(
            ExtractStoryboardSpecification(Destination('/video.story.jpg'), 5, 6, 256, 512, 'jpg', 12.25)
        ).execute()

        assert_that(group.jobs[0], instance_of(ExtractStoryboardJob))
        assert_that(group.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'specifications': [{
                            'rows': 6,
                            'tileHeight': 512,
                            'format': 'jpg',
                            'tileWidth': 256,
                            'destination': {
                                'directory': None,
                                'path': '/video.story.jpg',
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'segmentDuration': 12.25,
                            'columns': 5
                        }],
                        'sources': [{
                            'path': '/video.mp4',
                            'fileId': None
                        }],
                        'jobCallback': None
                    }))
