import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_

from media_platform import Source
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.import_file_job import ImportFileSpecification
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.job.transcode.video_qualities import VideoQualityRange, VideoQuality
from media_platform.job.transcode_job import TranscodeSpecification
from media_platform.metadata.audio.audio_extra_metadata import Image, Lyrics, AudioExtraMetadata
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL
from media_platform.service.flow_control_service.callback_specification import CallbackSpecification
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.flow_control_service.flow import Flow
from media_platform.service.flow_control_service.flow_control_service import FlowControlService
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.rest_result import RestResult
from tests.service.flow_control_service.test_flows.flow_state_response import flow_state_response
from tests.service.flow_control_service.test_flows.invoke_flow1_request import invoke_flow1_request
from tests.service.flow_control_service.test_flows.invoke_flow1_response import invoke_flow1_response
from tests.service.flow_control_service.test_flows.invoke_flow_callback_request import invoke_flow_callback_request
from tests.service.flow_control_service.test_flows.invoke_flow_callback_response import invoke_flow_callback_response
from tests.service.flow_control_service.test_flows.invoke_flow_replace_extra_metadata_request import \
    invoke_flow_replace_extra_metadata_request
from tests.service.flow_control_service.test_flows.invoke_flow_replace_extra_metadata_response import \
    invoke_flow_replace_extra_metadata_response

transcode_specification = TranscodeSpecification(
    Destination(directory='/deliverables/'),
    quality_range=VideoQualityRange(VideoQuality.res_720p, VideoQuality.res_1080p))

import_file_specification = ImportFileSpecification('http://movs.me/video.mp4', Destination('/imports/video.mp4'))

audio_source_path = '/source/path.mp3'
audio_destination_path = '/destination/path.mp3'
audio_source = Source(audio_source_path)
audio_destination = Destination(audio_destination_path, None, ACL.private)

image = Image('image_url', 'mime_type', 'image_description')
lyrics = Lyrics('text', 'eng', 'lyrics_description')

extra_metadata = AudioExtraMetadata('track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer',
                                    'year', image, lyrics)

replace_extra_metadata_specification = ReplaceAudioExtraMetadataSpecification(audio_source, audio_destination,
                                                                              extra_metadata)


class TestFlowControlService(unittest.TestCase):
    authenticator = None  # type: AppAuthenticator
    authenticated_http_client = None  # type: AuthenticatedHTTPClient
    flow_control_service = None  # type: FlowControlService

    @classmethod
    def setUpClass(cls):
        cls.authenticator = AppAuthenticator('app', 'secret')
        cls.authenticated_http_client = AuthenticatedHTTPClient(cls.authenticator)
        cls.flow_control_service = FlowControlService('fish.barrel', cls.authenticated_http_client)

    @httpretty.activate
    def test_invoke_flow1_request(self):
        self._register_invoke_request(invoke_flow1_response)

        flow_state = self.flow_control_service.invoke_flow_request().set_invocation(
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

        self._assert_flow(flow_state, invoke_flow1_request)

    @httpretty.activate
    def test_invoke_flow_replace_extra_metadata(self):
        self._register_invoke_request(invoke_flow_replace_extra_metadata_response)

        flow_state = self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['metadata1'])
        ).set_flow(
            Flow().add_component(
                'metadata1',
                Component(ComponentType.replace_extra_metadata, [], replace_extra_metadata_specification)
            )
        ).execute()

        self._assert_flow(flow_state, invoke_flow_replace_extra_metadata_request)

    @httpretty.activate
    def test_invoke_flow_callback(self):
        self._register_invoke_request(invoke_flow_callback_response)
        flow_state = self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['import1'])
        ).set_flow(
            Flow().add_component(
                'import1',
                Component(ComponentType.import_file, ['callback1'], import_file_specification)
            ).add_component(
                'callback1',
                Component(ComponentType.callback,
                          [],
                          CallbackSpecification('http://requestbin.fullcontact.com/sc9kxnsc',
                                                {'attachment-key': 'attachment-value'},
                                                {'header': 'value'}))
            )
        ).execute()

        self._assert_flow(flow_state, invoke_flow_callback_request)

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
    def _register_invoke_request(response_payload):
        response = RestResult(0, 'OK', response_payload)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/flow_control/flow',
            body=json.dumps(response.serialize())
        )

    def _assert_flow(self, flow_state, request_payload):
        assert_that(flow_state, instance_of(FlowState))
        self.assertEqual(json.loads(httpretty.last_request().body), request_payload)
