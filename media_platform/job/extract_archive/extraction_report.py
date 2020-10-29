from __future__ import annotations

from media_platform.service.destination import Destination
from media_platform.lang.serialization import Serializable, Deserializable


class ExtractionReportFormat:
    csv = 'csv'
    json = 'json'

    @classmethod
    def has_value(cls, value: str or ExtractionReportFormat):
        return value in [cls.csv, cls.json]


class ExtractionReport(Serializable, Deserializable):
    def __init__(self, destination: Destination, report_format: ExtractionReportFormat = ExtractionReportFormat.csv):
        self.destination = destination
        self.format = report_format

    @classmethod
    def deserialize(cls, data: dict) -> ExtractionReport:
        destination = Destination.deserialize(data['destination'])

        return ExtractionReport(destination, data['format'])

    def serialize(self) -> dict:
        return {
            'destination': self.destination.serialize(),
            'format': self.format
        }
