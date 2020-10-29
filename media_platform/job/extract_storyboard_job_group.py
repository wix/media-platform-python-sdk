from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class ExtractStoryboardJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ExtractStoryboardJobGroup:
        return cast(ExtractStoryboardJobGroup, super().deserialize(data))
