from media_platform.job.job import Job
from media_platform.job.job_deserializer import _JobDeserializer
from media_platform.lang.serialization import Deserializable


class _JobGroupResponse(Deserializable):
    def __init__(self, jobs):
        # type: ([Job]) -> None
        super(_JobGroupResponse, self).__init__()

        self.jobs = jobs

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> _JobGroupResponse
        return _JobGroupResponse(
            [_JobDeserializer.deserialize(item) for item in data]
        )
