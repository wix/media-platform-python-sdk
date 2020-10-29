from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class SubsetFontJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> SubsetFontJobGroup:
        return cast(SubsetFontJobGroup, super().deserialize(data))
