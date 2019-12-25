from typing import Optional

from media_platform.lang.serialization import Serializable


class Inline(Serializable):
    def __init__(self, file_name=None):
        # type: (Optional[str]) -> None
        super(Inline, self).__init__()

        self.file_name = file_name

    def set_file_name(self, file_name):
        # type: (str) -> Inline
        self.file_name = file_name
        return self

    def serialize(self):
        # type: () -> dict
        return {
            'filename': self.file_name
        }
