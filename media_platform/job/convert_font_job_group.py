from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class ConvertFontJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ConvertFontJobGroup:
        return cast(ConvertFontJobGroup, super().deserialize(data))
