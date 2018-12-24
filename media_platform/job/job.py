from datetime import datetime

from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Deserializable, Serializable
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
        self.group_id = group_id
        self.job_key = job_key

    @classmethod
    def deserialize(cls, data):
        # type: (str) -> JobID
        parts = data.split('_')
        return JobID(parts[0], parts[1])


class Job(Deserializable, Serializable):
    specification_type = None
    type = None

    def __init__(self, job_id, issuer, status, specification, sources=None, callback=None, flow_id=None,
                 result=None, date_created=None, date_updated=None):
        # type: (str, str, str, Specification or dict, [Source], Callback, str, RestResult, datetime, datetime) -> None

        _id = JobID.deserialize(job_id)  # type: JobID

        self.id = job_id
        self.group_id = _id.group_id
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
        specification = data['specification']
        if cls.specification_type:
            specification = cls.specification_type.deserialize(specification)

        result_data = data.get('result')
        if result_data:
            # todo: deserialize result payload as specific type
            result = RestResult.deserialize(result_data)
        else:
            result = None

        job = cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                  data.get('flowId'), result, date_created, date_updated)
        job.type = data['type']
        return job

    def serialize(self):
        return {
            'type': self.type,
            'groupId': self.group_id,
            'id': self.id,
            'issuer': self.issuer,
            'status': self.status,
            'specification': (self.specification.serialize() if isinstance(self.specification, Serializable)
                              else self.specification),
            'sources': [s.serialize() for s in self.sources],
            'callback': self.callback.serialize() if self.callback else None,
            'flowId': self.flow_id,
            'result': self.result.serialize() if self.result else None,
            'dateCreated': datetime_serialization.serialize(self.date_created),
            'dateUpdated': datetime_serialization.serialize(self.date_updated),
        }
