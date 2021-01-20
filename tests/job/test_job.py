from unittest import TestCase

from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveJob, ExtractArchiveSpecification
from media_platform.job.extract_archive.extraction_report import ExtractionReportFormat, ExtractionReport
from media_platform.job.job import Job, JobStatus
from media_platform.job.job_type import JobType
from media_platform.job.result.extract_archive_result import ExtractArchiveResult
from media_platform.job.result.transcode_result import TranscodeResult
from media_platform.job.transcode.video_qualities import VideoQuality
from media_platform.job.transcode_job import TranscodeJob, TranscodeSpecification
from media_platform.lang import datetime_serialization
from media_platform.service.destination import Destination
from media_platform.service.file_descriptor import ACL, FileDescriptor, FileType
from media_platform.service.source import Source

source = Source('/source.jpg')
destination = Destination('/path.png', acl=ACL.private)

extraction_report = ExtractionReport(Destination('/report.json', acl=ACL.private), ExtractionReportFormat.json)

frozen_time = datetime_serialization.deserialize('2001-12-25T00:00:00Z')

report_file = FileDescriptor(destination.path, 'report-file-id', FileType.file, 'application/json', 123, ACL.private,
                             date_created=frozen_time, date_updated=frozen_time)
extract_archive_result = ExtractArchiveResult(0, 'OK', extraction_report, report_file)
extract_archive_specification = ExtractArchiveSpecification(source, destination, extraction_report)

transcode_specification = TranscodeSpecification(destination, quality=VideoQuality.res_360p)
transcode_result = TranscodeResult(
    file_descriptor=FileDescriptor(
        '/path.mp4', 'file-id', FileType.file, 'video/mp4', 123, ACL.private, date_created=frozen_time,
        date_updated=frozen_time),
    master_ffmpeg_command='command',
    error_class='error_class'
)

extract_archive_job = ExtractArchiveJob(
    'group-id_job-key', 'urn:member:xxx', JobStatus.pending, extract_archive_specification, [source],
    result=extract_archive_result,
    date_created=frozen_time, date_updated=frozen_time)

extract_archive_data = {
    'status': 'pending',
    'dateCreated': '2001-12-25T00:00:00Z',
    'sources': [source.serialize()],
    'result': extract_archive_result.serialize(),
    'id': 'group-id_job-key',
    'issuer': 'urn:member:xxx',
    'specification': extract_archive_specification.serialize(),
    'groupId': 'group-id',
    'flowId': None,
    'dateUpdated': '2001-12-25T00:00:00Z',
    'callback': None,
    'type': JobType.extract_archive
}

transcode_job = TranscodeJob(
    'group-id_job-key', 'urn:member:xxx', JobStatus.pending, transcode_specification, [source],
    result=transcode_result, date_created=frozen_time, date_updated=frozen_time
)

transcode_data = {
    'status': 'pending',
    'dateCreated': '2001-12-25T00:00:00Z',
    'sources': [source.serialize()],
    'result': transcode_result.serialize(),
    'id': 'group-id_job-key',
    'issuer': 'urn:member:xxx',
    'specification': transcode_specification.serialize(),
    'groupId': 'group-id',
    'flowId': None,
    'dateUpdated': '2001-12-25T00:00:00Z',
    'callback': None,
    'type': JobType.transcode
}


class TestJob(TestCase):
    def test_serialize_extract_archive_job(self):
        serialized = extract_archive_job.serialize()
        self.assertEqual(extract_archive_data, serialized)

    def test_deserialize_extract_archive_job(self):
        deserialized = ExtractArchiveJob.deserialize(extract_archive_data)
        self.assertEqual(extract_archive_data, deserialized.serialize())

    def test_serialize_transcode_job(self):
        serialized = transcode_job.serialize()
        self.assertEqual(transcode_data, serialized)

    def test_deserialize_transcode_job(self):
        deserialized = TranscodeJob.deserialize(transcode_data)
        self.assertEqual(transcode_data, deserialized.serialize())

    def test_deserialize_untyped_job(self):
        deserialized = Job.deserialize(extract_archive_data)
        self.assertEqual(extract_archive_data, deserialized.serialize())
