from unittest import TestCase
from hamcrest import *

from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL
from media_platform.service.job_group import JobGroup
from media_platform.service.source import Source


class TestJobGroup(TestCase):

    def test_deserialize(self):
        source = Source('/source.jpg')
        destination = Destination('/path.png', acl=ACL.private)

        data = {
            'groupId': 'group-id',
            'jobs': [{
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
            }]
        }

        job_group = JobGroup.deserialize(data)

        assert_that(job_group.group_id, is_('group-id'))
