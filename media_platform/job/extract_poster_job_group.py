from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class ExtractPosterJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ExtractPosterJobGroup:
        return cast(ExtractPosterJobGroup, super().deserialize(data))
