from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.extract_archive.extraction_report import ExtractionReport
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractArchiveResult(JobResult):
    type = JobType.extract_archive

    def __init__(self, code=None, message=None, extraction_report=None, report_file_descriptor=None):
        # type: (int, str, ExtractionReport, FileDescriptor) -> None
        super(ExtractArchiveResult, self).__init__(code, message)

        self.extraction_report = extraction_report
        self.report_file_descriptor = report_file_descriptor

    @classmethod
    def deserialize(cls, data):
        # type: (dict or None) -> ExtractArchiveResult or None
        if data is None:
            return None

        result = JobResult.deserialize(data)
        payload = data.get('payload') or {}
        extracted_files_report_data = payload.get('extractedFilesReport')
        report_file_descriptor_data = payload.get('reportFileDescriptor')

        result.extraction_report = cls._get_extraction_report(extracted_files_report_data)
        result.report_file_descriptor = cls._get_report_file_descriptor(report_file_descriptor_data)
        result.__class__ = ExtractArchiveResult
        return result

    def serialize(self):
        # type: () -> dict
        data = super(ExtractArchiveResult, self).serialize()
        payload = {}
        if self.extraction_report:
            payload['extractedFilesReport'] = self.extraction_report.serialize()

        if self.report_file_descriptor:
            payload['reportFileDescriptor'] = self.report_file_descriptor.serialize()

        data['payload'] = payload

        return data

    @classmethod
    def _get_extraction_report(cls, extraction_report_data):
        if not extraction_report_data:
            return None

        return ExtractionReport.deserialize(extraction_report_data)

    @classmethod
    def _get_report_file_descriptor(cls, report_file_data):
        if not report_file_data:
            return None

        return FileDescriptor.deserialize(report_file_data)
