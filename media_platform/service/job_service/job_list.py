from media_platform.job.job import Job
# noinspection PyProtectedMember
from media_platform.job.job_deserializer import _JobDeserializer
from media_platform.lang.serialization import Deserializable


class JobList(Deserializable):
    def __init__(self, next_page_token, jobs):
        # type: (str, [Job]) -> None
        super(JobList, self).__init__()

        self.next_page_token = next_page_token
        self.jobs = jobs

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> JobList

        jobs = [_JobDeserializer.deserialize(j) for j in data['jobs']]

        return JobList(data['nextPageToken'], jobs)
