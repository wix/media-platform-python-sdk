from __future__ import annotations

from media_platform.metadata.audio.audio_basic import AudioBasic
from media_platform.metadata.audio.audio_extra import AudioExtra
from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.metadata.security.antivirus import ThreatDetectionMetadata
from media_platform.service.file_descriptor import FileDescriptor


class AudioFileMetadata(FileMetadata):
    def __init__(self, file_descriptor: FileDescriptor, basic: AudioBasic = None, extra: AudioExtra = None,
                 threat_detection: ThreatDetectionMetadata = None):
        super().__init__(MediaType.audio, file_descriptor, basic, threat_detection)

        self.extra = extra

    @classmethod
    def deserialize(cls, data: dict) -> AudioFileMetadata:
        if data['mediaType'] != MediaType.audio:
            raise ValueError('not audio metadata')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = AudioBasic.deserialize(data.get('basic')) if data.get('basic') else None
        extra = AudioExtra.deserialize(data.get('extra')) if data.get('extra') else None
        threat_detection = ThreatDetectionMetadata.deserialize(data.get('threatDetection')) \
            if data.get('threatDetection') else None

        return AudioFileMetadata(file_descriptor, basic, extra, threat_detection)
