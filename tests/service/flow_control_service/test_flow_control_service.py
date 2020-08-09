import json
import unittest
from typing import Dict

import httpretty
from hamcrest import assert_that, instance_of

from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.convert_font_job import ConvertFontSpecification, FontType
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.service.audio_service.audio_extra_metadata import Image, Lyrics, AudioExtraMetadata
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.flow_control_service.flow import Flow
from media_platform.service.flow_control_service.flow_control_service import FlowControlService
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.flow_control_service.operation import OperationStatus
from media_platform.service.flow_control_service.specifications.add_sources_specification import AddSourcesSpecification
from media_platform.service.flow_control_service.specifications.copy_file_specification import CopyFileSpecification
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from tests.service.flow_control_service.test_flows.flow_state.response import flow_state_response

import_file_specification = ImportFileSpecification('http://movs.me/video.mp4', Destination('/imports/video.mp4'))


class TestFlowControlService(unittest.TestCase):
    authenticator: AppAuthenticator = None
    authenticated_http_client: AuthenticatedHTTPClient = None
    flow_control_service: FlowControlService = None

    @classmethod
    def setUpClass(cls):
        cls.authenticator = AppAuthenticator('app', 'secret')
        cls.authenticated_http_client = AuthenticatedHTTPClient(cls.authenticator)
        cls.flow_control_service = FlowControlService('fish.barrel', cls.authenticated_http_client)

    @httpretty.activate
    def test_invoke_flow1_request(self):
        self._register_invoke_flow_response()

        transcode_specification = TranscodeSpecification(
            Destination(directory='/deliverables/'),
            quality_range=VideoQualityRange(VideoQuality.res_720p, VideoQuality.res_1080p))

        result = self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['import'])
        ).set_flow(
            Flow().add_component(
                'import',
                Component(ComponentType.import_file, ['transcode'], import_file_specification)
            ).add_component(
                'transcode',
                Component(ComponentType.transcode, ['playlist'], transcode_specification)
            ).add_component(
                'playlist',
                Component(ComponentType.playlist, [])
            )
        ).execute()

        self.assertIsNone(result)

    @httpretty.activate
    def test_invoke_flow_convert_font(self):
        self._register_invoke_flow_response()

        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['convert-font'], [Source('/source/font.ttf')])
        ).set_flow(
            Flow().add_component(
                'convert-font',
                Component(ComponentType.convert_font, [],
                          ConvertFontSpecification(
                              Destination('/destination/font.woff', None, ACL.private), FontType.woff))
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_copy_file(self):
        self._register_invoke_flow_response()

        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['copyfile1'], [Source('/source/path.txt')])
        ).set_flow(
            Flow().add_component(
                'copyfile1',
                Component(ComponentType.copy_file, [],
                          CopyFileSpecification(Destination('/destination/path.txt')))
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_replace_extra_metadata(self):
        self.maxDiff = None

        extra_metadata = AudioExtraMetadata(
            'track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer', 'year',
            Image('image_url', 'mime_type', 'image_description'), Lyrics('text', 'eng', 'lyrics_description'))

        self._register_invoke_flow_response()

        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['metadata1'], [Source('/source/path.mp3')])
        ).set_flow(
            Flow().add_component(
                'metadata1',
                Component(ComponentType.replace_extra_metadata, [],
                          ReplaceAudioExtraMetadataSpecification(
                              Destination('/destination/path.mp3', None, ACL.private), extra_metadata))
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_with_add_sources(self):
        self._register_invoke_flow_response()

        extra_metadata = AudioExtraMetadata(
            'track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer', 'year',
            Image('image_url', 'mime_type', 'image_description'), Lyrics('text', 'eng', 'lyrics_description'))

        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['addSources1', 'addSources2'], [])
        ).set_flow(
            Flow().add_component(
                'addSources1',
                Component(ComponentType.add_sources, ['metadata1'],
                          AddSourcesSpecification([Source('/source/path.mp3')]))
            ).add_component(
                'addSources2',
                Component(ComponentType.add_sources, ['metadata2'],
                          AddSourcesSpecification([Source('/source/path2.mp3')]))
            ).add_component(
                'metadata1',
                Component(ComponentType.replace_extra_metadata, [],
                          ReplaceAudioExtraMetadataSpecification(
                              Destination('/destination/path.mp3', None, ACL.private), extra_metadata))
            ).add_component(
                'metadata2',
                Component(ComponentType.replace_extra_metadata, [],
                          ReplaceAudioExtraMetadataSpecification(
                              Destination('/destination/path2.mp3', None, ACL.private), extra_metadata))
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_with_group_wait(self):
        self._register_invoke_flow_response()

        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['copy1', 'copy2'], [Source('/source/path.txt')])
        ).set_flow(
            Flow().add_component(
                'copy1',
                Component(ComponentType.copy_file, ['group-wait'],
                          CopyFileSpecification(Destination('/destination/path1.txt')))
            ).add_component(
                'copy2',
                Component(ComponentType.copy_file, ['group-wait'],
                          CopyFileSpecification(Destination('/destination/path2.txt')))
            ).add_component(
                'group-wait',
                Component(ComponentType.group_wait, [])
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_with_component_callback(self):
        self._register_invoke_flow_response()
        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['import1'], operation_callback_status_filter={OperationStatus.error, OperationStatus.success})
        ).set_flow(
            Flow().add_component(
                'import1',
                Component(ComponentType.import_file, [], import_file_specification,
                          callback=Callback('http://requestbin.fullcontact.com/sc9kxnsc',
                                            {'attachment-key': 'attachment-value'},
                                            {'header': 'value'}))
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_with_callback(self):
        self._register_invoke_flow_response()
        self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['import1'],
                       callback=Callback('http://requestbin.fullcontact.com/sc9kxnsc',
                                         {'attachment-key': 'attachment-value'},
                                         {'header': 'value'}))
        ).set_flow(
            Flow().add_component(
                'import1',
                Component(ComponentType.import_file, [], import_file_specification)
            )
        ).execute()

    @httpretty.activate
    def test_invoke_flow_missing_successors(self):
        with self.assertRaises(ValueError) as context:
            self.flow_control_service.invoke_flow_request().set_invocation(
                Invocation('import1')
            ).set_flow(
                Flow().add_component('import1',
                                     Component(ComponentType.import_file, ['missing-successor-name'],
                                               import_file_specification))
            ).execute()

        self.assertEqual(str(context.exception), 'Missing successor components: [\'missing-successor-name\']')

    @httpretty.activate
    def test_flow_state_request(self):
        response = RestResult(0, 'OK', flow_state_response)
        httpretty.register_uri(
            httpretty.GET,
            'https://fish.barrel/_api/flow_control/flow/state-id',
            body=json.dumps(response.serialize())
        )

        flow_state = self.flow_control_service.flow_state_request().set_id('state-id').execute()

        assert_that(flow_state, instance_of(FlowState))

    @httpretty.activate
    def test_abort_flow_request(self):
        response = RestResult(0, 'OK', None)
        httpretty.register_uri(
            httpretty.DELETE,
            'https://fish.barrel/_api/flow_control/flow/state-id',
            body=json.dumps(response.serialize())
        )

        self.flow_control_service.abort_flow_request().set_id('state-id').execute()

    @staticmethod
    def _register_invoke_flow_response():
        response = RestResult(0, 'OK')
        httpretty.register_uri(httpretty.POST, 'https://fish.barrel/_api/flow_control/flow',
                               body=json.dumps(response.serialize()))

    def _assert_flow(self, expected_request_payload, response_flow_state):
        assert_that(response_flow_state, instance_of(FlowState))
        self._normalize_request_payload(expected_request_payload)
        request_payload = json.loads(httpretty.last_request().body)
        self._normalize_request_payload(request_payload)

        self.assertEqual(expected_request_payload, request_payload)

    @staticmethod
    def _normalize_request_payload(request_payload: Dict):
        request_payload['invocation']['operationCallbackStatusFilter'].sort()
