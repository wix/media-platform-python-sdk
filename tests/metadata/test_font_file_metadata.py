from unittest import TestCase
from hamcrest import assert_that, is_

from media_platform.metadata.file_metadata_deserializer import _FileMetadataDeserializer


class TestFontFileMetadata(TestCase):

    def test_deserialize(self):
        data = {
            'basic': {
                'fontType': 'ttf',
                'name': None,
                'family': None
            },
            'mediaType': 'font',
            'fileDescriptor': {
                'mimeType': 'font/ttf',
                'hash': None,
                'dateCreated': '2000-12-25T00:00:00Z',
                'id': 'id',
                'path': '/fish.ttf',
                'lifecycle': None,
                'size': 2323,
                'urn': 'urn:file:id',
                'acl': 'public',
                'dateUpdated': '2000-12-25T00:00:00Z',
                'type': '-'
            }}

        file_metadata = _FileMetadataDeserializer.deserialize(data)

        assert_that(file_metadata.media_type, is_('font'))
