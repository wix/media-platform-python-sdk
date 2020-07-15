from __future__ import annotations

from media_platform.job.job_group import JobGroup


class ExtractStoryboardJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ExtractStoryboardJobGroup:
        return super(ExtractStoryboardJobGroup, cls).deserialize(data)
