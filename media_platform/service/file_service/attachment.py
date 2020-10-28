from __future__ import annotations

from media_platform.lang.serialization import Serializable


class Attachment(Serializable):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def set_file_name(self, file_name: str) -> Attachment:
        self.file_name = file_name
        return self

    def serialize(self) -> dict:
        return {
            'filename': self.file_name
        }
