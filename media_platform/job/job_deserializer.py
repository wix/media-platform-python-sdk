from media_platform.job.import_file_job import ImportFileJob
from media_platform.job.job import Job
from media_platform.lang.serialization import Deserializable


class _JobDeserializer(Deserializable):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Job
        job_type = data['type']

        if job_type == ImportFileJob.type:
            return ImportFileJob.deserialize(data)
        else:
            return Job.deserialize(data)
