from __future__ import annotations

from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.security.antivirus import ThreatDetectionMetadata
from media_platform.metadata.video.video_basic import VideoBasic
from media_platform.service.file_descriptor import FileDescriptor


class VideoFileMetadata(FileMetadata):
    def __init__(self, file_descriptor: FileDescriptor, basic: VideoBasic = None,
                 threat_detection: ThreatDetectionMetadata = None):
        super().__init__(MediaType.video, file_descriptor, basic, threat_detection)

    @classmethod
    def deserialize(cls, data: dict) -> VideoFileMetadata:
        if data['mediaType'] != MediaType.video:
            raise ValueError('not video metadata')

        basic_data = data.get('basic')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = VideoBasic.deserialize(basic_data) if basic_data else None
        threat_detection = ThreatDetectionMetadata.deserialize(data.get('threatDetection')) \
            if data.get('threatDetection') else None

        return VideoFileMetadata(file_descriptor, basic, threat_detection)
