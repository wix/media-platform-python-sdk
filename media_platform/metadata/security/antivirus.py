from __future__ import annotations

import datetime

from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Serializable, Deserializable


class AntivirusMetadata(Serializable, Deserializable):
    def __init__(self, infected: bool, signature: str, timestamp: datetime.datetime):
        self.infected = infected
        self.signature = signature
        self.timestamp = timestamp

    @classmethod
    def deserialize(cls, data: dict) -> AntivirusMetadata:
        return AntivirusMetadata(
            data.get('infected'),
            data.get('signature'),
            datetime_serialization.deserialize(data['scanTimestamp'])
        )

    def serialize(self) -> dict:
        return {
            'infected': self.infected,
            'signature': self.signature,
            'scanTimestamp': self.timestamp
        }


class ThreatDetectionMetadata(Serializable, Deserializable):
    def __init__(self, antivirus: AntivirusMetadata = None):
        self.antivirus = antivirus

    @classmethod
    def deserialize(cls, data: dict) -> ThreatDetectionMetadata:
        return ThreatDetectionMetadata(AntivirusMetadata.deserialize(data.get('antivirus')))

    def serialize(self) -> dict:
        return {
            'antivirus': self.antivirus.serialize()
        }
