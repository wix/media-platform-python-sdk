from unittest import TestCase
from hamcrest import assert_that, is_

from media_platform.metadata.file_metadata_deserializer import _FileMetadataDeserializer


class TestVideoFileMetadata(TestCase):

    def test_deserialize(self):
        data = {
            'basic': {
                'transparency': 'not_transparent',
                'tbr': None,
                'interlaced': False,
                'videoStreams': [{
                    'codecLongName': 'long fish',
                    'height': 200,
                    'pixelFormat': '?',
                    'duration': 321,
                    'bitrate': 123,
                    'index': 0,
                    'rotate': None,
                    'rFrameRate': '25/1',
                    'codecTag': 'fish',
                    'avgFrameRate': '25/1',
                    'codecName': 'h264',
                    'width': 100,
                    'sampleAspectRatio': '1:1',
                    'displayAspectRatio': '16:9',
                    'fieldOrder': None,
                    'disposition': []
                }], 'audioStreams': [{
                    'codecLongName': 'long axx',
                    'index': 0,
                    'channelLayout': 'd',
                    'codecTag': 'acc',
                    'duration': 122,
                    'codecName': 'axx',
                    'bitrate': 12212,
                    'sampleRate': 41000,
                    'channels': 2
                }], 'format': None},
            'mediaType': 'video',
            'fileDescriptor': {
                'mimeType': 'video/mp4',
                'hash': None,
                'dateUpdated': '2000-12-25T00:00:00Z',
                'dateCreated': '2000-12-25T00:00:00Z',
                'path': '/fish.mp4',
                'urn': 'urn:file:id',
                'acl': 'public',
                'type': '-',
                'lifecycle': None,
                'id': 'id',
                'size': 2323
            }
        }

        file_metadata = _FileMetadataDeserializer.deserialize(data)

        assert_that(file_metadata.media_type, is_('video'))
