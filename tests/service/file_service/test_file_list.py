from unittest import TestCase
from hamcrest import *

from media_platform.service.file_descriptor import FileType, ACL
from media_platform.service.file_service.file_list import FileList


class TestFileList(TestCase):

    def test_deserialize(self):
        files_data = {
            'nextPageToken': 'token',
            'files': [{
                'id': 'moshe',
                'path': '/client/images/animals/cat.jpg',
                'type': FileType.file,
                'mimeType': 'image/jpg',
                'size': 15431,
                'acl': ACL.private,
                'hash': 'bulldog'
            }]}

        file_list = FileList.deserialize(files_data)

        assert_that(file_list.files[0].file_id, is_('moshe'))
        assert_that(file_list.next_page_token, is_('token'))
