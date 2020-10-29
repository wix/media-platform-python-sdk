from __future__ import annotations

from media_platform.job.job import Job
from media_platform.lang.serialization import Deserializable
# noinspection PyProtectedMember
from media_platform.job.job_deserializer import _JobDeserializer


class _JobGroupResponse(Deserializable):
    def __init__(self, jobs: [Job]):
        self.jobs = jobs

    @classmethod
    def deserialize(cls, data: dict) -> _JobGroupResponse:
        return _JobGroupResponse(
            [_JobDeserializer.deserialize(item) for item in data]
        )
