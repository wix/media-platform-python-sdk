from unittest import TestCase
from hamcrest import *

from media_platform.service.file_descriptor import FileDescriptor, FileType
from media_platform.service.file_service.file_upload_callback_payload import FileUploadCallbackPayload


class TestFileUploadCallbackPayload(TestCase):

    def test_deserialize(self):
        file_descriptor = FileDescriptor('/fish.jpg', 'file-id', FileType.file, 'image/jpg', 1200).serialize()

        data = {
            'file': file_descriptor,
            'attachment': {'dog': 'bull'}
        }

        payload = FileUploadCallbackPayload.deserialize(data)

        assert_that(payload.attachment, is_({'dog': 'bull'}))
        assert_that(payload.file_descriptor.file_id, is_('file-id'))
