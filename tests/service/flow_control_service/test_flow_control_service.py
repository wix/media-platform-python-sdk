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
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.flow_control_service.flow import Flow
from media_platform.service.flow_control_service.flow_control_service import FlowControlService
from media_platform.service.flow_control_service.flow_state import FlowState
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.rest_result import RestResult
from tests.service.flow_control_service.test_flows.flow_state_response import flow_state_response
from tests.service.flow_control_service.test_flows.invoke_flow1_request import invoke_flow1_request
from tests.service.flow_control_service.test_flows.invoke_flow1_response import invoke_flow1_response
from tests.service.flow_control_service.test_flows.invoke_flow_replace_extra_metadata_request import \
    invoke_flow_replace_extra_metadata_request
from tests.service.flow_control_service.test_flows.invoke_flow_replace_extra_metadata_response import \
    invoke_flow_replace_extra_metadata_response


class TestFlowControlService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    flow_control_service = FlowControlService('fish.barrel', authenticated_http_client)

    @httpretty.activate
    def test_invoke_flow1_request(self):
        response = RestResult(0, 'OK', invoke_flow1_response)
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
        assert_that(json.loads(httpretty.last_request().body), is_(invoke_flow1_request))

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
    def test_flow_state_request(self):
        response = RestResult(0, 'OK', None)
        httpretty.register_uri(
            httpretty.DELETE,
            'https://fish.barrel/_api/flow_control/flow/state-id',
            body=json.dumps(response.serialize())
        )

        self.flow_control_service.abort_flow_request().set_id('state-id').execute()

    @httpretty.activate
    def test_invoke_flow_replace_extra_metadata(self):
        source_path = '/source/path.mp3'
        destination_path = '/destination/path.mp3'
        source = Source(source_path)
        destination = Destination(destination_path, None, ACL.private)

        image = Image('image_url', 'mime_type', 'image_description')
        lyrics = Lyrics('text', 'eng', 'lyrics_description')

        extra_metadata = AudioExtraMetadata('track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer',
                                            'year', image, lyrics)

        specification = ReplaceAudioExtraMetadataSpecification(source, destination, extra_metadata)

        response = RestResult(0, 'OK', invoke_flow_replace_extra_metadata_response)
        httpretty.register_uri(
            httpretty.POST,
            'https://fish.barrel/_api/flow_control/flow',
            body=json.dumps(response.serialize())
        )

        flow_state = self.flow_control_service.invoke_flow_request().set_invocation(
            Invocation(['metadata1'])
        ).set_flow(
            Flow().add_component(
                'metadata1',
                Component(ComponentType.replace_extra_metadata, [], specification)
            )
        ).execute()

        assert_that(flow_state, instance_of(FlowState))
        self.assertEqual(json.loads(httpretty.last_request().body), invoke_flow_replace_extra_metadata_request)
