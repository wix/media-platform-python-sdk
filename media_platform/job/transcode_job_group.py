from __future__ import annotations

from typing import cast

from media_platform.job.job_group import JobGroup


class TranscodeJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> TranscodeJobGroup:
        return cast(TranscodeJobGroup, super().deserialize(data))
