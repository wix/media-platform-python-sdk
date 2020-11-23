from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class ScanFileJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ScanFileJobGroup:
        return cast(ScanFileJobGroup, super().deserialize(data))
