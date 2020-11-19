from __future__ import annotations

from media_platform.job.convert_font_job import ConvertFontJob
from media_platform.job.create_archive_job import CreateArchiveJob
from media_platform.job.extract_archive.extract_archive_job import ExtractArchiveJob
from media_platform.job.extract_poster_job import ExtractPosterJob
from media_platform.job.extract_storyboard_job import ExtractStoryboardJob
from media_platform.job.import_file_job import ImportFileJob
from media_platform.job.job import Job
from media_platform.job.replace_extra_metadata_job import ReplaceExtraMetadataJob
from media_platform.job.subset_font_job import SubsetFontJob
from media_platform.job.transcode_job import TranscodeJob
from media_platform.job.scan_file_job import ScanFileJob
from media_platform.lang.serialization import Deserializable


class _JobDeserializer(Deserializable):
    _job_classes = [
        ImportFileJob,
        ExtractPosterJob,
        ExtractStoryboardJob,
        CreateArchiveJob,
        ExtractArchiveJob,
        TranscodeJob,
        ReplaceExtraMetadataJob,
        ConvertFontJob,
        SubsetFontJob,
        ScanFileJob
    ]

    _type_to_class = {c.type: c for c in _job_classes}

    @classmethod
    def deserialize(cls, data: dict) -> Job:
        job_type = data['type']
        job_class = cls._type_to_class.get(job_type, Job)
        return job_class.deserialize(data)
