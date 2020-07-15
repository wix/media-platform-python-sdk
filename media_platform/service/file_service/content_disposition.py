from __future__ import annotations


class ContentDisposition:
    class Type:
        attachment = 'attachment'
        inline = 'inline'

    def __init__(self, file_name: str = None, disposition_type: Type = Type.attachment):
        self.file_name = file_name
        self.disposition_type = disposition_type

    def set_file_name(self, file_name: str) -> ContentDisposition:
        self.file_name = file_name
        return self

    def set_type(self, disposition_type: Type) -> ContentDisposition:
        self.disposition_type = disposition_type
        return self

    def serialize(self) -> dict:
        return {
            'filename': self.file_name,
            'type': self.disposition_type
        }
