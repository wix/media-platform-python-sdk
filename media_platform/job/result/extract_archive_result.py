from __future__ import annotations

from media_platform.service.file_descriptor import FileDescriptor
from media_platform.job.extract_archive.extraction_report import ExtractionReport
from media_platform.job.job_type import JobType
from media_platform.job.result.job_result import JobResult


class ExtractArchiveResult(JobResult):
    type = JobType.extract_archive

    def __init__(self, code: int = None, message: str = None, extraction_report: ExtractionReport = None,
                 file_descriptor: FileDescriptor = None):
        super().__init__(code, message)
        self.extraction_report = extraction_report
        self.file_descriptor = file_descriptor

    @classmethod
    def deserialize(cls, data: dict or None) -> ExtractArchiveResult or None:
        if data is None:
            return None

        result = JobResult.deserialize(data)
        result.__class__ = ExtractArchiveResult

        payload = data.get('payload') or {}
        extracted_files_report_data = payload.get('extractedFilesReport')
        report_file_descriptor_data = payload.get('reportFileDescriptor')

        result.extraction_report = cls._get_extraction_report(extracted_files_report_data)
        result.file_descriptor = cls._get_report_file_descriptor(report_file_descriptor_data)
        return result

    def serialize(self) -> dict:
        data = super().serialize()
        payload = {}
        if self.extraction_report:
            payload['extractedFilesReport'] = self.extraction_report.serialize()

        if self.file_descriptor:
            payload['reportFileDescriptor'] = self.file_descriptor.serialize()

        data['payload'] = payload

        return data

    @classmethod
    def _get_extraction_report(cls, extraction_report_data: dict or None) -> ExtractionReport or None:
        if not extraction_report_data:
            return None

        return ExtractionReport.deserialize(extraction_report_data)

    @classmethod
    def _get_report_file_descriptor(cls, report_file_data: dict or None) -> FileDescriptor or None:
        if not report_file_data:
            return None

        return FileDescriptor.deserialize(report_file_data)
