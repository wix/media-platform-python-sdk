import json
from datetime import datetime
from unittest import TestCase

import httpretty
from hamcrest import assert_that, is_

from media_platform import FileDescriptor, Destination, Source
from media_platform.auth.app_authenticator import AppAuthenticator
from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.replace_extra_metadata_job import ReplaceAudioExtraMetadataSpecification
from media_platform.metadata.audio.audio_extra_metadata import Image, Lyrics, AudioExtraMetadata
from media_platform.service.file_descriptor import FileType, ACL
from media_platform.service.rest_result import RestResult
from media_platform.service.audio_service.audio_service import AudioService

source_path = '/source/path.mp3'
destination_path = '/destination/path.mp3'
source = Source(source_path)
destination = Destination(destination_path, None, ACL.private)

image = Image('image_url', 'mime_type', 'image_description')
lyrics = Lyrics('text', 'lang', 'lyrics_description')

extra_metadata = AudioExtraMetadata('track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer', 'year',
                                    image, lyrics)

specification = ReplaceAudioExtraMetadataSpecification(source, destination, extra_metadata)

file_id = 'file_id'
audio_mime_type = 'audio/mp3'
frozen_time = datetime(2011, 11, 11, 11, 11, 11)
audio_file_descriptor = FileDescriptor(destination_path, file_id, FileType.file, audio_mime_type, 123, ACL.private,
                                       file_hash='file_hash', date_created=frozen_time, date_updated=frozen_time)


class TestAudioService(TestCase):

    @classmethod
    def setUpClass(cls):
        authenticator = AppAuthenticator('app', 'secret')
        authenticated_http_client = AuthenticatedHTTPClient(authenticator)
        cls.audio_service = AudioService('domain', authenticated_http_client)

    @httpretty.activate
    def test_replace_extra_metadata_request(self):
        response_body = RestResult(0, 'OK', audio_file_descriptor.serialize())

        httpretty.register_uri(
            httpretty.PUT,
            'https://domain/_api/av/extra-metadata',
            body=json.dumps(response_body.serialize())
        )

        got_file_descriptor = self.audio_service.replace_extra_metadata_request().set_specification(
            specification
        ).execute()

        assert_that(got_file_descriptor.serialize(), is_(audio_file_descriptor.serialize()))