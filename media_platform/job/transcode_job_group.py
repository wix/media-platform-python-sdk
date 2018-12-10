from media_platform.job.job_group import JobGroup


class TranscodeJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> TranscodeJobGroup

        return super(TranscodeJobGroup, cls).deserialize(data)
