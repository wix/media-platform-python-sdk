from __future__ import annotations

from media_platform.job.job_type import JobType
from media_platform.job.specification import Specification
from media_platform.job.job import Job


class ScanFileSpecification(Specification):
    def serialize(self) -> dict:
        return {}

    @classmethod
    def deserialize(cls, data: dict) -> ScanFileSpecification:
        return cls()


class ScanFileJob(Job):
    type = JobType.av_scan
    specification_type = ScanFileSpecification
