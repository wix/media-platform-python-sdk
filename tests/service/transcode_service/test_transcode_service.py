import json
import unittest

import httpretty
from hamcrest import assert_that, instance_of, is_
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.transcode.audio_qualities import AudioQuality
from media_platform.job.transcode.video_qualities import VideoQuality, VideoQualityRange
from media_platform.job.transcode_job import TranscodeSpecification, TranscodeJob
from media_platform.job.transcode.clipping import Clipping
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import FileDescriptor, FileType
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source
from media_platform.service.transcode_service.transcode_service import TranscodeService
from tests.service.transcode_service.test_files.transcode1_request import transcode1_request
from tests.service.transcode_service.test_files.transcode1_response import transcode1_response
from tests.service.transcode_service.test_files.transcode_clip_request import transcode_clip_request
from tests.service.transcode_service.test_files.transcode_clip_response import transcode_clip_response


class TestTranscodeService(unittest.TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)

    transcode_service = TranscodeService('fish.appspot.com', authenticated_http_client)

    @httpretty.activate
    def test_transcode_request(self):
        self._register_transcode_request(transcode1_response)

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
        assert_that(json.loads(httpretty.last_request().body), is_(transcode1_request))

    @httpretty.activate
    def test_transcode_audio_clipping(self):
        self._register_transcode_request(transcode_clip_response)

        group = self.transcode_service.transcode_request().add_sources(
            Source('/audio.mp3')
        ).add_specifications(
            TranscodeSpecification(
                Destination(directory='/'),
                quality=AudioQuality.aac_128,
                clipping=Clipping(clip_start=3,
                                  clip_end=6,
                                  fade_in_duration=1,
                                  fade_out_duration=2,
                                  fade_in_offset=4,
                                  fade_out_offset=5)
            )
        ).execute()

        assert_that(group.jobs[0], instance_of(TranscodeJob))
        self.assertEqual(group.group_id, 'g')
        self.assertEqual(json.loads(httpretty.last_request().body), transcode_clip_request)

    def test_playlist_request(self):
        url = self.transcode_service.playlist_request().add_files(
            FileDescriptor('/movie.720.mp4', 'file-id', FileType.file, 'video/mp4', 123)
        ).add_paths('/movie.1080p.mp4').execute()

        assert_that(url, is_('//packager-fish.wixmp.com/movie.,720,1080p,.mp4.urlset/master.m3u8'))

    @staticmethod
    def _register_transcode_request(response_body):
        response = RestResult(0, 'OK', response_body)
        httpretty.register_uri(httpretty.POST, 'https://fish.appspot.com/_api/av/transcode',
                               json.dumps(response.serialize()))
