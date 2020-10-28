from __future__ import annotations

from media_platform.job.job import Job
from media_platform.lang.serialization import Deserializable
# noinspection PyProtectedMember
from media_platform.job.job_deserializer import _JobDeserializer


class JobList(Deserializable):
    def __init__(self, next_page_token: str, jobs: [Job]):
        self.next_page_token = next_page_token
        self.jobs = jobs

    @classmethod
    def deserialize(cls, data: dict) -> JobList:
        jobs = [_JobDeserializer.deserialize(j) for j in data['jobs']]

        return JobList(data['nextPageToken'], jobs)
