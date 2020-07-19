from __future__ import annotations

from datetime import datetime

from media_platform.job.result.job_result import JobResult
from media_platform.job.result.job_result_deserializer import JobResultDeserializer
from media_platform.job.specification import Specification
from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.callback import Callback
from media_platform.service.source import Source


class JobStatus:
    pending = 'pending'
    working = 'working'
    success = 'success'
    error = 'error'


class JobID(Deserializable):
    def __init__(self, group_id: str, job_key: str):
        self.group_id = group_id
        self.job_key = job_key

    @classmethod
    def deserialize(cls, data: str) -> JobID:
        parts = data.split('_')
        return JobID(parts[0], parts[1])


class Job(Deserializable, Serializable):
    specification_type = None
    type = None

    def __init__(self, job_id: str, issuer: str, status: JobStatus, specification: Specification,
                 sources: [Source] = None, callback: Callback = None, flow_id: str = None,
                 result: JobResult = None, date_created: datetime = None, date_updated: datetime = None):
        _id = JobID.deserialize(job_id)

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
    def deserialize(cls, data: dict) -> Job:
        sources = [Source.deserialize(source) for source in data['sources']]
        date_created = datetime_serialization.deserialize(data['dateCreated'])
        date_updated = datetime_serialization.deserialize(data['dateUpdated'])
        callback_data = data.get('callback')
        callback = Callback.deserialize(callback_data) if callback_data else None
        specification = data['specification']
        if cls.specification_type:
            specification = cls.specification_type.deserialize(specification)

        result_data = data.get('result')
        result = JobResultDeserializer.deserialize(data['type'], result_data) if result_data else None

        job = cls(data['id'], data['issuer'], data['status'], specification, sources, callback,
                  data.get('flowId'), result, date_created, date_updated)
        job.type = data['type']
        return job

    def serialize(self) -> dict:
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
