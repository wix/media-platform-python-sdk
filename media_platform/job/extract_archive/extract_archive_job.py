from __future__ import annotations

from media_platform.job.extract_archive.extraction_report import ExtractionReport
from media_platform.job.job import Job
from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.service.destination import Destination
from media_platform.service.source import Source


class ExtractArchiveSpecification(Specification):
    def __init__(self, source: Source, destination: Destination, extraction_report: ExtractionReport = None):
        self.source = source
        self.destination = destination
        self.extraction_report = extraction_report

    @classmethod
    def deserialize(cls, data: dict) -> ExtractArchiveSpecification:
        extraction_report_data = data.get('extractedFilesReport')
        if extraction_report_data:
            extraction_report = ExtractionReport.deserialize(extraction_report_data)
        else:
            extraction_report = None

        source_data = data.get('source')
        source = Source.deserialize(source_data) if source_data else None
        return ExtractArchiveSpecification(source,
                                           Destination.deserialize(data['destination']),
                                           extraction_report)

    def serialize(self) -> dict:
        return {
            'source': self.source.serialize() if self.source else None,
            'destination': self.destination.serialize(),
            'extractedFilesReport': self.extraction_report.serialize() if self.extraction_report else None
        }


class ExtractArchiveJob(Job):
    type = JobType.extract_archive
    specification_type = ExtractArchiveSpecification
