from time import sleep

from typing import List

from demo.globals import client
from media_platform import FileDescriptor
from media_platform.job.job import JobStatus, Job
from media_platform.job.job_group import JobGroup
from media_platform.job.result.extract_archive_result import ExtractArchiveResult
from media_platform.job.result.transcode_result import TranscodeResult


def wait_for_result_files(job_group):
    # type: (JobGroup) -> List[FileDescriptor]
    return [wait_for_result(j).file_descriptor for j in job_group.jobs]


def wait_for_result(job):
    # type: (Job) -> [TranscodeResult or ExtractArchiveResult]
    while job.status not in [JobStatus.success, JobStatus.error]:
        sleep(1)
        job = client.job_service.job_request(). \
            set_id(job.id). \
            execute()

    if job.status == JobStatus.error:
        raise Exception(job.result.message)

    return job.result
