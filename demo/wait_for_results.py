from __future__ import annotations

from time import sleep

from demo.globals import client
from media_platform.job.job import JobStatus, Job
from media_platform.job.result.job_result import JobResult


def wait_for_result(job: Job) -> JobResult:
    while job.status not in [JobStatus.success, JobStatus.error]:
        sleep(1)

        job = client.job_service.job_request().set_id(job.job_id).execute()

    if job.status == JobStatus.error:
        raise Exception(job.result.message)

    return job.result
