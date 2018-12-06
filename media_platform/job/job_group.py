from media_platform.job.job import Job
from media_platform.job.job_deserializer import _JobDeserializer
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
        jobs = [_JobDeserializer.deserialize(job) for job in data['jobs']]

        return cls(data['groupId'], jobs)
