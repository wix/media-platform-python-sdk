from media_platform.job.create_archive_job import CreateArchiveJob
from media_platform.job.extract_archive_job import ExtractArchiveJob
from media_platform.job.extract_poster_job import ExtractPosterJob
from media_platform.job.extract_storyboard_job import ExtractStoryboardJob
from media_platform.job.import_file_job import ImportFileJob
from media_platform.job.job import Job
from media_platform.job.transcode_job import TranscodeJob
from media_platform.lang.serialization import Deserializable


class _JobDeserializer(Deserializable):

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Job
        job_type = data['type']

        if job_type == ImportFileJob.type:
            return ImportFileJob.deserialize(data)
        if job_type == ExtractPosterJob.type:
            return ExtractPosterJob.deserialize(data)
        if job_type == ExtractStoryboardJob.type:
            return ExtractStoryboardJob.deserialize(data)
        if job_type == CreateArchiveJob.type:
            return CreateArchiveJob.deserialize(data)
        if job_type == ExtractArchiveJob.type:
            return ExtractArchiveJob.deserialize(data)
        if job_type == TranscodeJob.type:
            return TranscodeJob.deserialize(data)
        else:
            return Job.deserialize(data)
