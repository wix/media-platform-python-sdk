from media_platform.job.job_group import JobGroup


class ExtractStoryboardJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ExtractStoryboardJobGroup

        return super(ExtractStoryboardJobGroup, cls).deserialize(data)
