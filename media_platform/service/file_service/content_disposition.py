from typing import Optional


class ContentDisposition(object):
    class Type(object):
        attachment = 'attachment'
        inline = 'inline'

    def __init__(self, file_name=None, type=Type.attachment):
        # type: (Optional[str], Type) -> None
        self.file_name = file_name
        self.type = type

    def set_file_name(self, file_name):
        # type: (str) -> ContentDisposition
        self.file_name = file_name
        return self

    def set_type(self, type):
        # type: (Type) -> ContentDisposition
        self.type = type
        return self

    def serialize(self):
        # type: () -> dict
        return {
            'filename': self.file_name,
            'type': self.type
        }
