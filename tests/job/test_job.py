from unittest import TestCase
from hamcrest import *

from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL
from media_platform.job.job import Job
from media_platform.service.source import Source


class TestJob(TestCase):

    def test_deserialize(self):
        source = Source('/source.jpg')
        destination = Destination('/path.png', acl=ACL.private)

        data = {
            'status': 'pending',
            'dateCreated': '2001-12-25T00:00:00Z',
            'sources': [source.serialize()],
            'result': None,
            'id': 'group-id_job-key',
            'issuer': 'urn:member:xxx',
            'specification': {
                'source': source.serialize(),
                'destination': destination.serialize(),
                'extractedFilesReport': {
                    'destination': destination.serialize(),
                    'format': 'json'
                }
            },
            'groupId': 'group-id',
            'flowId': None,
            'dateUpdated': '2001-12-25T00:00:00Z',
            'type': 'urn:job:archive.extract'
        }

        job = Job.deserialize(data)

        assert_that(job.id, is_('group-id_job-key'))
