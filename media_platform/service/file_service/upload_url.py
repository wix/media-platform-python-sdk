from media_platform.lang.serialization import Deserializable


class UploadUrl(Deserializable):
    def __init__(self, upload_url, upload_token):
        # type: (str, str) -> None
        super(UploadUrl, self).__init__()

        self.upload_url = upload_url
        self.upload_token = upload_token

    @classmethod
    def deserialize(cls, data):
        return UploadUrl(data['uploadUrl'], data['uploadToken'])
