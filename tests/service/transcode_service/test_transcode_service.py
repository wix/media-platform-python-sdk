import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.transcode.video_qualities import VideoQuality, VideoQualityRange
from media_platform.job.transcode_job import TranscodeSpecification, TranscodeJob
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor, FileType
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from media_platform.service.transcode_service.transcode_service import TranscodeService


class TestTranscodeService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    transcode_service = TranscodeService('fish.appspot.com', authenticated_http_client)

    @httpretty.activate
    def test_transcode_request(self):
        payload = {
            'jobs': [
                {
                    'issuer': 'urn:app:app-id',
                    'type': 'urn:job:av.transcode',
                    'id': 'g_1',
                    'groupId': 'g',
                    'status': 'pending',
                    'sources': [
                        {
                            'path': '/video.mp4',
                            'fileId': 'source-id'
                        }
                    ],
                    'specification': {
                        'quality': '480p',
                        'destination': {
                            'directory': None,
                            'path': '/video.480p.mp4',
                            'acl': 'public'
                        },
                        'video': {
                            'type': 'video',
                            'specification': {
                                'filter': 'scale=768:480,setsar=1/1',
                                'frameRate': '25.0',
                                'codec': {
                                    'profile': 'main',
                                    'maxRate': 6000000,
                                    'crf': 20,
                                    'name': 'h.264',
                                    'level': '3.1'
                                },
                                'resolution': {
                                    'width': 768,
                                    'height': 480
                                },
                                'keyFrame': 50
                            }
                        },
                        'audio': {
                            'type': 'audio',
                            'specification': {
                                'channels': 'stereo',
                                'codec': {
                                    'cbr': 3112,
                                    'name': 'aac'
                                }
                            }
                        }
                    },
                    'result': None,
                    'dateUpdated': '2017-06-25T12:13:32Z',
                    'dateCreated': '2017-06-25T12:13:32Z',
                },
                {
                    'issuer': 'urn:app:app-id',
                    'type': 'urn:job:av.transcode',
                    'id': 'g_2',
                    'groupId': 'g',
                    'status': 'pending',
                    'sources': [
                        {
                            'path': '/video.mp4',
                            'fileId': 'source-id'
                        }
                    ],
                    'specification': {
                        'quality': '720p',
                        'destination': {
                            'directory': None,
                            'path': '/video.720p.mp4',
                            'acl': 'public'
                        },
                        'video': {
                            'type': 'video',
                            'specification': {
                                'filter': 'scale=1152:720,setsar=1/1',
                                'frameRate': '25.0',
                                'codec': {
                                    'profile': 'high',
                                    'maxRate': 6000000,
                                    'crf': 20,
                                    'name': 'h.264',
                                    'level': '4.1'
                                },
                                'resolution': {
                                    'width': 1152,
                                    'height': 720
                                },
                                'keyFrame': 50
                            }
                        },
                        'audio': {
                            'type': 'audio',
                            'specification': {
                                'channels': 'stereo',
                                'codec': {
                                    'cbr': 3112,
                                    'name': 'aac'
                                }
                            }
                        }
                    },
                    'result': None,
                    'dateUpdated': '2017-06-25T12:13:33Z',
                    'dateCreated': '2017-06-25T12:13:33Z',
                },
            ],
            'groupId': 'g'
        }
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.appspot.com/_api/av/transcode',
            body=json.dumps(response.serialize())
        )

        group = self.transcode_service.transcode_request().add_sources(
            Source('/video.mp4')
        ).add_specifications(
            TranscodeSpecification(
                Destination(directory='/'),
                quality_range=VideoQualityRange(
                    minimum=VideoQuality.res_480p,
                    maximum=VideoQuality.res_1080p,
                )
            )
        ).execute()

        assert_that(group.jobs[0], instance_of(TranscodeJob))
        assert_that(group.group_id, is_('g'))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'specifications': [{
                            'video': None,
                            'destination': {
                                'directory': '/',
                                'path': None,
                                'lifecycle': None,
                                'acl': 'public'
                            },
                            'quality': None,
                            'qualityRange': {
                                'minimum': '480p',
                                'maximum': '1080p'
                            },
                            'audio': None
                        }],
                        'sources': [{
                            'path': '/video.mp4',
                            'fileId': None
                        }],
                        'jobCallback': None
                    }))

    def test_playlist_request(self):
        url = self.transcode_service.playlist_request().add_files(
            FileDescriptor('/movie.720.mp4', 'file-id', FileType.file, 'video/mp4', 123)
        ).add_paths('/movie.1080p.mp4').execute()

        assert_that(url, is_('https://packager-fish.wixmp.com/movie.,720,1080p,.mp4.urlset/master.m3u8'))
