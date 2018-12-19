import json
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


class TestAudioService(TestCase):
    authenticator = AppAuthenticator('app', 'secret')
    authenticated_http_client = AuthenticatedHTTPClient(authenticator)
    audio_service = AudioService('domain', authenticated_http_client)

    @httpretty.activate
    def test_replace_extra_metadata_request(self):
        file_descriptor = FileDescriptor('/destination.mp3', 'id', FileType.file, 'audio/mp3', 123,
                                         ACL.private).serialize()
        response_body = RestResult(0, 'OK', file_descriptor)

        httpretty.register_uri(
            httpretty.PUT,
            'https://domain/_api/av/extra-metadata',
            body=json.dumps(response_body.serialize())
        )

        result = self.audio_service.replace_extra_metadata_request().set_specification(
            ReplaceAudioExtraMetadataSpecification(
                Source('/source.mp3'),
                Destination('/destination.mp3', acl=ACL.private),
                AudioExtraMetadata('track_name', 'artist', 'album_name', 'track_number', 'genre', 'composer', 'year',
                                   Image('image_url', 'mime_type', 'image_description'),
                                   Lyrics('text', 'lang', 'lyrics_description')))
        ).execute()

        assert_that(result.serialize(), is_(file_descriptor))
