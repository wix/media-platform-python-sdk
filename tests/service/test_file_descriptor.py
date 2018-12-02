from unittest import TestCase
from hamcrest import *

from media_platform.service.file_descriptor import FileType, ACL, FileDescriptor


class TestFileDescriptor(TestCase):

    def test_deserialize(self):
        file_data = {
            'id': 'moshe',
            'path': '/client/images/animals/cat.jpg',
            'type': FileType.file,
            'mimeType': 'image/jpg',
            'size': 15431,
            'acl': ACL.private,
            'hash': 'bulldog'
        }

        file_descriptor = FileDescriptor.deserialize(file_data)

        assert_that(file_descriptor.id, is_(file_data['id']))
        assert_that(file_descriptor.path, is_(file_data['path']))

    def test_serialize(self):
        file_data = {
            'path': '/client/images/animals/cat.jpg',
            'type': FileType.file,
            'mimeType': 'image/jpg',
            'size': 15431,
            'acl': ACL.private,
            'hash': '324234234',
            'id': '123456789',
            'lifecycle': {
                'age': 500,
                'action': 'delete'
            },
            'dateUpdated': '2017-01-01T00:00:00Z',
            'dateCreated': '2017-01-01T00:00:00Z'
        }

        file_descriptor = FileDescriptor.deserialize(file_data)

        assert_that(file_descriptor.serialize(), is_(file_data))
