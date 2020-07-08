from __future__ import annotations

from media_platform.error_code import ErrorCode
from media_platform.job.job_type import JobType
from media_platform.job.result.convert_font_result import ConvertFontResult
from media_platform.job.result.create_archive_result import CreateArchiveResult
from media_platform.job.result.extract_archive_result import ExtractArchiveResult
from media_platform.job.result.extract_poster_result import ExtractPosterResult
from media_platform.job.result.extract_storyboard_result import ExtractStoryboardResult
from media_platform.job.result.import_file_result import ImportFileResult
from media_platform.job.result.job_callback_failed_result import JobCallbackFailedResult
from media_platform.job.result.job_result import JobResult
from media_platform.job.result.job_timeout_result import JobTimeoutResult
from media_platform.job.result.replace_audio_extra_metadata_result import ReplaceAudioExtraMetadataResult
from media_platform.job.result.subset_font_result import SubsetFontResult
from media_platform.job.result.transcode_result import TranscodeResult


class JobResultDeserializer:
    _result_classes = [
        CreateArchiveResult,
        ExtractArchiveResult,
        ExtractPosterResult,
        ExtractStoryboardResult,
        ImportFileResult,
        ReplaceAudioExtraMetadataResult,
        TranscodeResult,
        ConvertFontResult,
        SubsetFontResult,
    ]

    _type_to_class = {c.type: c for c in _result_classes}

    @classmethod
    def deserialize(cls, job_type: JobType, data: dict) -> JobResult or None:
        if data['code'] == ErrorCode.job_callback_failed:
            job_result_class = JobCallbackFailedResult

        elif data['code'] == ErrorCode.job_timeout:
            job_result_class = JobTimeoutResult

        else:
            job_result_class = cls._type_to_class.get(job_type, JobResult)

        return job_result_class.deserialize(data)
