from media_platform.service.job import Job
from media_platform.lang.serialization import Deserializable


class JobGroup(Deserializable):
    def __init__(self, group_id, jobs):
        # type: (str, [Job]) -> None
        super(JobGroup, self).__init__()
        self.group_id = group_id
        self.jobs = jobs

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> JobGroup
        jobs = [Job.deserialize(job) for job in data['jobs']]

        return JobGroup(data['groupId'], jobs)
