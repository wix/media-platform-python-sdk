from datetime import datetime


ISO_DATE_WITH_MILLIS_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
ISO_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def deserialize(iso_date):
    # type: (str) -> datetime or None

    if iso_date is None:
        return None

    if '.' in iso_date:
        return datetime.strptime(iso_date, ISO_DATE_WITH_MILLIS_FORMAT)
    else:
        return datetime.strptime(iso_date, ISO_DATE_FORMAT)


def serialize(date_time=datetime.utcnow()):
    # type: (datetime) -> str

    return date_time.strftime(ISO_DATE_FORMAT)
