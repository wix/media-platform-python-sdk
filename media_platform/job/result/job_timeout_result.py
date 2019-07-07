from datetime import timedelta

from media_platform.error_code import ErrorCode
from media_platform.job.result.job_result import JobResult


class JobTimeoutResult(JobResult):
    type = None

    def __init__(self, job_id, timeout):
        # type: (str, timedelta) -> None
        super(JobTimeoutResult, self).__init__(ErrorCode.job_timeout, 'Job %s timed out after %s' % (job_id, timeout))
