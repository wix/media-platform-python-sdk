from unittest import TestCase

from media_platform.job.extract_archive_job import ExtractArchiveJob, ExtractArchiveSpecification, ExtractionReport, \
    ExtractionReportFormat
from media_platform.lang import datetime_serialization
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL
from media_platform.job.job import Job
from media_platform.service.source import Source

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
    'type': 'urn:job:archive.extract',
    'callback': None
}

frozen_time = datetime_serialization.deserialize('2001-12-25T00:00:00Z')

extraction_report = ExtractionReport(destination, ExtractionReportFormat.json)
specification = ExtractArchiveSpecification(source, destination, extraction_report)
job = ExtractArchiveJob('group-id_job-key', 'urn:member:xxx', 'pending', specification, [source],
                        date_created=frozen_time, date_updated=frozen_time)


class TestJob(TestCase):
    def test_serialize(self):
        serialized = job.serialize()
        self.assertEqual(serialized, data)

    def test_deserialize_typed_job(self):
        deserialized = ExtractArchiveJob.deserialize(data)
        self.assertEqual(deserialized.serialize(), data)

    def test_deserialize_untyped_job(self):
        deserialized = Job.deserialize(data)
        self.assertEqual(deserialized.serialize(), data)
