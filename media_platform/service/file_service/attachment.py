from media_platform.lang.serialization import Serializable


class Attachment(Serializable):
    def __init__(self, file_name):
        # type: (str) -> None
        super(Attachment, self).__init__()

        self.file_name = file_name

    def set_file_name(self, file_name):
        # type: (str) -> Attachment
        self.file_name = file_name
        return self

    def serialize(self):
        # type: () -> dict
        return {
            'filename': self.file_name
        }
