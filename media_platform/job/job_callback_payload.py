from media_platform.job.job import Job
from media_platform.lang.serialization import Deserializable


class JobCallbackPayload(Deserializable):
    def __init__(self, job, attachment=None):
        # type: (Job, dict or None) -> None
        self.job = job
        self.attachment = attachment

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> JobCallbackPayload
        return cls(Job.deserialize(data['job']), data.get('attachment'))
