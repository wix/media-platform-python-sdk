from __future__ import annotations

from media_platform.error_code import ErrorCode
from media_platform.job.result.job_result import JobResult


class JobCallbackFailedResult(JobResult):
    type = None

    def __init__(self, message: str = None, job_result: dict = None):
        super(JobCallbackFailedResult, self).__init__(ErrorCode.job_callback_failed, message)
        self.job_result = job_result

    @classmethod
    def deserialize(cls, data: dict or None) -> JobCallbackFailedResult or None:
        if not data:
            return None

        payload = data.get('payload') or {}
        result = JobResult.deserialize(data)
        result.job_result = payload.get('jobResult')

        result.__class__ = JobCallbackFailedResult

        return result

    def serialize(self) -> dict:
        data = super(JobCallbackFailedResult, self).serialize()
        data['payload'] = {
            'jobResult': self.job_result
        }

        return data
