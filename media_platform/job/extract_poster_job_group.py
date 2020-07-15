from __future__ import annotations

from media_platform.job.job_group import JobGroup


class ExtractPosterJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> ExtractPosterJobGroup:
        return super(ExtractPosterJobGroup, cls).deserialize(data)
