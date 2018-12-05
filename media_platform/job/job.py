from datetime import datetime

from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Deserializable
from media_platform.service.callback import Callback
from media_platform.service.rest_result import RestResult
from media_platform.service.source import Source


class JobStatus(object):
    pending = 'pending'
    working = 'working'
    success = 'success'
    error = 'error'


class JobID(Deserializable):
    def __init__(self, group_id, job_key):
        # type: (str, str) -> None
        self.job_key = job_key
        self.group_id = group_id

    @classmethod
    def deserialize(cls, data):
        # type: (str) -> JobID
        parts = data.split('_')
        return JobID(parts[0], parts[1])


class Job(Deserializable):
    def __init__(self, job_id, job_type, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        # type: (str, str, str, str, Specification, [Source], Callback, str, RestResult, datetime, datetime) -> None

        _id = JobID.deserialize(job_id)  # type: JobID

        self.id = job_id
        self.group_id = _id.group_id
        self.type = job_type
        self.issuer = issuer
        self.status = status
        self.specification = specification
        self.sources = sources
        self.callback = callback
        self.flow_id = flow_id
        self.result = result
        self.date_created = date_created
        self.date_updated = date_updated

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Job

        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None

        return cls(data['id'], data['type'], data['issuer'], data['status'], data['specification'], sources, callback,
                   data.get('flowId'), data.get('result'), date_created, date_updated)
