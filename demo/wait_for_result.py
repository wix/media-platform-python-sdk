from time import sleep

from globals import client
from media_platform.job.job import JobStatus, Job


def wait_for_result(job):
    # type: (Job) -> Job
    while job.status not in [JobStatus.success, JobStatus.error]:
        sleep(1)
        job = client.job_service.job_request(). \
            set_id(job.id). \
            execute()

    if job.status == JobStatus.error:
        raise Exception(job.result.message)

    return job
