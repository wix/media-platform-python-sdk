from unittest import TestCase
from hamcrest import *

from media_platform.job.job_callback_payload import JobCallbackPayload
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL, FileDescriptor, FileType, FileMimeType
from media_platform.service.file_service.file_upload_callback_payload import FileUploadCallbackPayload
from media_platform.service.source import Source


class TestFileUploadCallbackPayload(TestCase):

    def test_deserialize(self):
        file_descriptor = FileDescriptor('/fish.jpg', 'file-id', FileType.file, 'image/jpg', 1200).serialize()

        data = {
            'file': file_descriptor,
            'attachment': {'dog': 'bull'}
        }

        payload = FileUploadCallbackPayload.deserialize(data)

        assert_that(payload.attachment, is_({'dog': 'bull'}))
        assert_that(payload.file_descriptor.id, is_('file-id'))
