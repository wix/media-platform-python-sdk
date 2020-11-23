from __future__ import annotations

from media_platform.lang.serialization import Deserializable
from media_platform.metadata.security.antivirus import ThreatDetectionMetadata
from media_platform.service.file_descriptor import FileDescriptor


class MediaType:
    undefined = ''
    image = 'image'
    video = 'video'
    audio = 'audio'
    font = 'font'


class FileMetadata(Deserializable):
    def __init__(self, media_type: str, file_descriptor: FileDescriptor, basic: Deserializable = None,
                 threat_detection: ThreatDetectionMetadata = None):
        self.media_type = media_type
        self.file_descriptor = file_descriptor
        self.basic = basic
        self.threat_detection = threat_detection

    @classmethod
    def deserialize(cls, data: dict) -> FileMetadata:
        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        threat_detection = ThreatDetectionMetadata.deserialize(data.get('threatDetection')) \
            if data.get('threatDetection') else None

        return FileMetadata(MediaType.undefined, file_descriptor, threat_detection=threat_detection)
