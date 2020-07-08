from __future__ import annotations

from media_platform.job.job_group import JobGroup


class SubsetFontJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> SubsetFontJobGroup:
        return super(SubsetFontJobGroup, cls).deserialize(data)
