from unittest import TestCase
from hamcrest import assert_that, is_

from media_platform.metadata.file_metadata_deserializer import _FileMetadataDeserializer


class TestAudioFileMetadata(TestCase):

    def test_deserialize(self):
        data = {
            'mediaType': '',
            'fileDescriptor': {
                'mimeType': 'text/plain',
                'hash': '4dfdsf',
                'dateCreated': '2000-12-25T00:00:00Z',
                'id': 'id',
                'path': '/fish.mp3',
                'lifecycle': None,
                'size': 2323,
                'urn': 'urn:file:id',
                'acl': 'public',
                'dateUpdated': '2000-12-25T00:00:00Z',
                'type': '-'
            }}

        file_metadata = _FileMetadataDeserializer.deserialize(data)

        assert_that(file_metadata.media_type, is_(''))
