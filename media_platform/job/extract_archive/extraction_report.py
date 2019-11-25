from media_platform.service.destination import Destination
from media_platform.lang.serialization import Serializable, Deserializable


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