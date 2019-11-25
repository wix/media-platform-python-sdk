from media_platform.job.job_group import JobGroup


class ConvertFontJobGroup(JobGroup):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ConvertFontJobGroup

        return super(ConvertFontJobGroup, cls).deserialize(data)
