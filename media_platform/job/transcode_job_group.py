from __future__ import annotations

from media_platform.job.job_group import JobGroup


class TranscodeJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data: dict) -> TranscodeJobGroup:
        return super(TranscodeJobGroup, cls).deserialize(data)
