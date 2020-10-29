from __future__ import annotations

from media_platform.job.job import Job
from media_platform.job.job_deserializer import _JobDeserializer
from media_platform.lang.serialization import Deserializable


class JobGroup(Deserializable):
    def __init__(self, group_id: str, jobs: [Job]):
        self.group_id = group_id
        self.jobs = jobs

    @classmethod
    def deserialize(cls, data: dict) -> JobGroup:
        jobs = [_JobDeserializer.deserialize(job) for job in data['jobs']]

        return cls(data['groupId'], jobs)
