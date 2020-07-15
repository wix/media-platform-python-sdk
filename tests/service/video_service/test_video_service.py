import json
import unittest

import httpretty

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.extract_poster_job import ExtractPosterSpecification, ExtractPosterJob, PosterImageFormat, \
    PosterFilter, PixelFormat
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
                    'percentage': None,
                    'destination': {
                        'path': '/video.poster.png',
                        'directory': '/',
                        'acl': 'public'
                    },
                    'format': 'png',
                    'filters': ['transparentCrop'],
                    'pixelFormat': 'rgba'
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
            ExtractPosterSpecification(20, Destination('/video.poster.png'), PosterImageFormat.png,
                                       filters=[PosterFilter.transparent_crop], pixel_format=PixelFormat.rgba)
        ).execute()

        self.assertIsInstance(group.jobs[0], ExtractPosterJob)
        self.assertEqual('g', group.group_id)
        self.assertEqual(
            {
                'specifications': [{
                    'second': 20,
                    'percentage': None,
                    'destination': {
                        'directory': None,
                        'path': '/video.poster.png',
                        'lifecycle': None,
                        'acl': 'public',
                        'bucket': None
                    },
                    'format': 'png',
                    'filters': ['transparentCrop'],
                    'pixelFormat': 'rgba'
                }],
                'sources': [{
                    'path': '/video.mp4',
                    'fileId': None
                }]
            }, json.loads(httpretty.last_request().body))

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

        self.assertIsInstance(group.jobs[0], ExtractStoryboardJob)
        self.assertEqual('g', group.group_id)
        self.assertEqual({
            'specifications': [{
                'rows': 6,
                'tileHeight': 512,
                'format': 'jpg',
                'tileWidth': 256,
                'destination': {
                    'directory': None,
                    'path': '/video.story.jpg',
                    'lifecycle': None,
                    'acl': 'public',
                    'bucket': None
                },
                'segmentDuration': 12.25,
                'columns': 5
            }],
            'sources': [{
                'path': '/video.mp4',
                'fileId': None
            }],
            'jobCallback': None
        }, json.loads(httpretty.last_request().body))
