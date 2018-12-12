import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.service.destination import Destination
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.flow_control_service.flow import Flow
from media_platform.service.flow_control_service.flow_control_service import FlowControlService
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.rest_result import RestResult


class TestFlowControlService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    flow_control_service = FlowControlService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_invoke_flow_request(self):
        payload = {
            'invocation': {
                'sources': [],
                'entryPoints': ['import'],
                'notification': None
            },
            'operations': {
                'import': {
                    'status': 'success',
                    'deleteSources': False,
                    'jobs': ['g_1'],
                    'specification': {
                        'destination': {
                            'directory': None,
                            'path': '/imports/video.mp4',
                            'acl': 'public',
                            'lifecycle': None
                        },
                        'sourceUrl': 'https://fish.com/dag.gadol'
                    },
                    'results': [
                        {
                            'mimeType': 'video/mp4',
                            'hash': None,
                            'urn': 'urn:file:123',
                            'dateCreated': '2018-01-11T13:15:57Z',
                            'path': '/imports/video.mp4',
                            'dateUpdated': '2018-01-11T13:15:57Z',
                            'acl': 'public',
                            'type': '-',
                            'id': 'abcd',
                            'size': 4151438,
                            'lifecycle': None
                        }
                    ],
                    'extraResults': {},
                    'sources': [],
                    'successors': [
                        'transcode'
                    ],
                    'type': 'file.import'
                },
                'transcode': {
                    'status': 'success',
                    'jobs': ['g2_1', 'g2_2', 'g2_3', 'g2_4', 'g2_5'],
                    'deleteSources': False,
                    'specification': {
                        'quality': None,
                        'destination': {
                            'directory': '/deliverables/',
                            'path': None,
                            'acl': 'public',
                            'lifecycle': None
                        },
                        'video': None,
                        'qualityRange': {
                            'minimum': '720p',
                            'maximum': '1080p'
                        },
                        'audio': None
                    },
                    'results': [
                        {
                            'mimeType': 'video/mp4',
                            'hash': '56566',
                            'dateCreated': '2018-01-10T16:11:36Z',
                            'path': '/deliverables/720p/video.mp4',
                            'dateUpdated': '2018-01-10T16:11:36Z',
                            'acl': 'public',
                            'type': '-',
                            'id': '2341234',
                            'size': 2607390,
                            'lifecycle': None
                        },
                        {
                            'mimeType': 'video/mp4',
                            'hash': '6773f38357a87b4a37681aa17620ae6c',
                            'dateCreated': '2018-01-10T16:11:42Z',
                            'path': '/deliverables/1080p/video.mp4',
                            'dateUpdated': '2018-01-10T16:11:42Z',
                            'acl': 'public',
                            'type': '-',
                            'id': '3243241',
                            'size': 5517966,
                            'lifecycle': None
                        }
                    ],
                    'extraResults': {},
                    'sources': [
                        {
                            'path': '/imports/video.mp4',
                            'fileId': '2345234534'
                        }
                    ],
                    'successors': [
                        'playlist'
                    ],
                    'type': 'av.transcode'
                },
                'playlist': {
                    'status': 'success',
                    'deleteSources': False,
                    'jobs': [],
                    'specification': None,
                    'results': [
                        {
                            'mimeType': 'video/mp4',
                            'hash': '56566',
                            'dateCreated': '2018-01-10T16:11:36Z',
                            'path': '/deliverables/720p/video.mp4',
                            'dateUpdated': '2018-01-10T16:11:36Z',
                            'acl': 'public',
                            'type': '-',
                            'id': '12341324',
                            'size': 2607390,
                            'lifecycle': None
                        },
                        {
                            'mimeType': 'video/mp4',
                            'hash': '6773f38357a87b4a37681aa17620ae6c',
                            'dateCreated': '2018-01-10T16:11:42Z',
                            'path': '/deliverables/1080p/video.mp4',
                            'dateUpdated': '2018-01-10T16:11:42Z',
                            'acl': 'public',
                            'type': '-',
                            'id': '21341324',
                            'size': 5517966,
                            'lifecycle': None
                        }
                    ],
                    'extraResults': {
                        'urlset': '//fishenzon.com/deliverables/,720p,1080p,/video.mp4.urlset/master.m3u8'
                    },
                    'sources': [
                        {
                            'path': '/deliverables/720p/video.mp4',
                            'fileId': '2341234'
                        },
                        {
                            'path': '/deliverables/1080p/video.mp4',
                            'fileId': '1234234'
                        }
                    ],
                    'successors': [],
                    'type': 'av.create_urlset'
                }
            },
            'id': '12342134',
            'status': 'success',
            'error': None
        }
        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/flow_control/flow',
            body=json.dumps(response.serialize())
        )

        flow_state = self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['import'])
        ).set_flow(
            Flow().add_component(
                'import',
                Component(ComponentType.import_file, ['transcode'],
                          ImportFileSpecification('http://movs.me/video.mp4', Destination('/imports/video.mp4')))
            ).add_component(
                'transcode',
                Component(ComponentType.transcode, ['playlist'],
                          TranscodeSpecification(Destination(directory='/deliverables/'),
                                                 quality_range=VideoQualityRange(VideoQuality.res_720p,
                                                                                 VideoQuality.res_1080p)))
            ).add_component(
                'playlist',
                Component(ComponentType.playlist, [])
            )
        ).execute()

        assert_that(flow_state, instance_of(FlowState))
        assert_that(json.loads(httpretty.last_request().body),
                    is_({
                        'invocation': {
                            'sources': [],
                            'entryPoints': ['import']
                        },
                        'flow': {
                            'import': {
                                'deleteSources': False,
                                'specification': {
                                    'sourceUrl': 'http://movs.me/video.mp4',
                                    'destination': {
                                        'directory': None,
                                        'path': '/imports/video.mp4',
                                        'lifecycle': None,
                                        'acl': 'public'
                                    }
                                },
                                'successors': ['transcode'],
                                'type': 'file.import'
                            },
                            'playlist': {
                                'deleteSources': False,
                                'specification': None,
                                'successors': [],
                                'type': 'av.create_urlset'
                            },
                            'transcode': {
                                'deleteSources': False,
                                'specification': {
                                    'video': None,
                                    'destination': {
                                        'directory': '/deliverables/',
                                        'path': None,
                                        'lifecycle': None,
                                        'acl': 'public'
                                    },
                                    'quality': None,
                                    'qualityRange': {
                                        'minimum': '720p',
                                        'maximum': '1080p'
                                    },
                                    'audio': None
                                },
                                'successors': ['playlist'],
                                'type': 'av.transcode'
                            }
                        }}))

    @httpretty.activate
    def test_flow_state_request(self):
        payload = {
                'invocation': {
                    'sources': [],
                    'entryPoints': [
                        'import'
                    ],
                    'notification': None
                },
                'operations': {
                    'import': {
                        'status': 'success',
                        'deleteSources': False,
                        'jobs': [
                            'g_1'
                        ],
                        'specification': {
                            'destination': {
                                'directory': None,
                                'path': '/imports/video.mp4',
                                'acl': 'public',
                                'lifecycle': None
                            },
                            'sourceUrl': 'https://fish.com/dag.gadol'
                        },
                        'results': [
                            {
                                'mimeType': 'video/mp4',
                                'hash': None,
                                'urn': 'urn:file:1354324',
                                'dateCreated': '2018-01-11T13:15:57Z',
                                'path': '/imports/video.mp4',
                                'dateUpdated': '2018-01-11T13:15:57Z',
                                'acl': 'public',
                                'type': '-',
                                'id': '1354324',
                                'size': 4151438,
                                'lifecycle': None
                            }
                        ],
                        'extraResults': {},
                        'sources': [],
                        'successors': [
                            'transcode'
                        ],
                        'type': 'file.import'
                    },
                    'transcode': {
                        'status': 'success',
                        'jobs': [
                            'g2_1',
                            'g2_2',
                        ],
                        'deleteSources': False,
                        'specification': {
                            'quality': None,
                            'destination': {
                                'directory': '/',
                                'path': None,
                                'acl': 'public',
                                'lifecycle': None
                            },
                            'video': None,
                            'qualityRange': {
                                'minimum': '480p',
                                'maximum': '1440p'
                            },
                            'audio': None
                        },
                        'results': [
                            {
                                'mimeType': 'video/mp4',
                                'hash': '123123213',
                                'dateCreated': '2018-01-10T16:11:30Z',
                                'path': '/video.480p.mp4',
                                'dateUpdated': '2018-01-10T16:11:30Z',
                                'acl': 'public',
                                'type': '-',
                                'id': '65454643',
                                'size': 1277825,
                                'lifecycle': None
                            },
                            {
                                'mimeType': 'video/mp4',
                                'hash': '56566',
                                'dateCreated': '2018-01-10T16:11:36Z',
                                'path': '/video.720p.mp4',
                                'dateUpdated': '2018-01-10T16:11:36Z',
                                'acl': 'public',
                                'type': '-',
                                'id': '45345',
                                'size': 2607390,
                                'lifecycle': None
                            }
                        ],
                        'extraResults': {},
                        'sources': [
                            {
                                'path': '/imports/video.mp4',
                                'fileId': '1354324'
                            }
                        ],
                        'successors': [
                            'playlist'
                        ],
                        'type': 'av.transcode'
                    },
                    'playlist': {
                        'status': 'success',
                        'deleteSources': False,
                        'jobs': [],
                        'specification': None,
                        'results': [
                            {
                                'mimeType': 'video/mp4',
                                'hash': '123123213',
                                'urn': 'urn:file:65454643',
                                'dateCreated': '2018-01-10T16:11:30Z',
                                'path': '/video.480p.mp4',
                                'dateUpdated': '2018-01-10T16:11:30Z',
                                'acl': 'public',
                                'type': '-',
                                'id': '65454643',
                                'size': 1277825,
                                'lifecycle': None
                            },
                            {
                                'mimeType': 'video/mp4',
                                'hash': '56566',
                                'dateCreated': '2018-01-10T16:11:36Z',
                                'path': '/video.720p.mp4',
                                'dateUpdated': '2018-01-10T16:11:36Z',
                                'acl': 'public',
                                'type': '-',
                                'id': '45345',
                                'size': 2607390,
                                'lifecycle': None
                            }
                        ],
                        'extraResults': {
                            'urlset': '//fishenzon.com/video.,480p,720p,.mp4.urlset/master.m3u8'
                        },
                        'sources': [
                            {
                                'path': '/video.480p.mp4',
                                'fileId': '65454643'
                            },
                            {
                                'path': '/video.720p.mp4',
                                'fileId': '45345'
                            }
                        ],
                        'successors': [],
                        'type': 'av.create_urlset'
                    }
                },
                'id': '49eca277747047c5833f15a0eed137b9',
                'status': 'success',
                'error': None
        }

        response = RestResult(0, 'OK', payload)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/flow_control/flow/state-id',
            body=json.dumps(response.serialize())
        )

        flow_state = self.flow_control_service.flow_state_request().set_id('state-id').execute()

        assert_that(flow_state, instance_of(FlowState))

    @httpretty.activate
    def test_flow_state_request(self):
        response = RestResult(0, 'OK', None)
        httpretty.register_uri(
            httpretty.DELETE,
            'https://fish.barrel/_api/flow_control/flow/state-id',
            body=json.dumps(response.serialize())
        )

        self.flow_control_service.abort_flow_request().set_id('state-id').execute()
