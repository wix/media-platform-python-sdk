from media_platform.job.job import Job
from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.callback import Callback
from media_platform.service.destination import Destination
from media_platform.service.rest_result import RestResult
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

        return ExtractArchiveSpecification(Source.deserialize(data['source']),
                                           Destination.deserialize(data['destination']),
                                           extraction_report)

    def serialize(self):
        # type: () -> dict
        return {
            'source': self.source.serialize(),
            'destination': self.destination.serialize(),
            'extractedFilesReport': self.extraction_report.serialize() if self.extraction_report else None
        }


class ExtractArchiveJob(Job):
    type = 'urn:job:archive.extract'

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        super(ExtractArchiveJob, self).__init__(job_id, self.type, issuer, status, specification, sources,
                                                callback, flow_id, result, date_created, date_updated)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractArchiveJob

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = ExtractArchiveSpecification.deserialize(data['specification'])
        if data.get('result'):
            result = RestResult.deserialize(data['result'])
        else:
            result = None

        return cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                   data.get('flowId'), result, date_created, date_updated)
