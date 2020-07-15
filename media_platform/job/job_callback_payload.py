from __future__ import annotations

from media_platform.job.job import Job
from media_platform.lang.serialization import Deserializable


class JobCallbackPayload(Deserializable):
    def __init__(self, job: Job, attachment: dict = None):
        self.job = job
        self.attachment = attachment

    @classmethod
    def deserialize(cls, data: dict) -> JobCallbackPayload:
        return cls(Job.deserialize(data['job']), data.get('attachment'))
