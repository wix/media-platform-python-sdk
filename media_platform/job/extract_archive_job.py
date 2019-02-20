from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.destination import Destination
from media_platform.service.source import Source


class ExtractionReportFormat(object):
    csv = 'csv'
    json = 'json'

    @classmethod
    def has_value(cls, value):
        return value in [cls.csv, cls.json]


class ExtractionReport(Serializable, Deserializable):
    def __init__(self, destination, report_format=ExtractionReportFormat.csv):
        # type: (Destination, ExtractionReportFormat) -> None
        super(ExtractionReport, self).__init__()

        self.destination = destination
        self.format = report_format

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractionReport
        destination = Destination.deserialize(data['destination'])

        return ExtractionReport(destination, data['format'])

    def serialize(self):
        # type: () -> dict
        return {
            'destination': self.destination.serialize(),
            'format': self.format
        }


class ExtractArchiveSpecification(Specification):
    def __init__(self, source, destination, extraction_report=None):
        # type: (Source, Destination, ExtractionReport or None) -> None

        self.source = source
        self.destination = destination
        self.extraction_report = extraction_report

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractArchiveSpecification

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

    def serialize(self):
        # type: () -> dict
        return {
            'source': self.source.serialize() if self.source else None,
            'destination': self.destination.serialize(),
            'extractedFilesReport': self.extraction_report.serialize() if self.extraction_report else None
        }


class ExtractArchiveJob(Job):
    type = 'urn:job:archive.extract'
    specification_type = ExtractArchiveSpecification
