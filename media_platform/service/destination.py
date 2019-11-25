from typing import Optional

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.file_descriptor import FileDescriptor, ACL
from media_platform.service.lifecycle import Lifecycle


class Destination(Serializable, Deserializable):
    def __init__(self, path=None, directory=None, acl=ACL.public, lifecycle=None, bucket=None):
        # type: (Optional[str], Optional[str], Optional[ACL], Optional[Lifecycle], Optional[str]) -> None
        super(Destination, self).__init__()

        self._validate_values(path, directory, acl)

        self.path = path
        self.directory = directory
        self.acl = acl or ACL.public
        self.lifecycle = lifecycle
        self.bucket = bucket

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Destination

        lifecycle_data = data.get('lifecycle')
        lifecycle = Lifecycle.deserialize(lifecycle_data) if lifecycle_data else None

        return cls(data.get('path'), data.get('directory'), data['acl'], lifecycle, data.get('bucket'))

    def serialize(self):
        # type: () -> dict
        return {
            'path': self.path,
            'directory': self.directory,
            'acl': self.acl,
            'lifecycle': self.lifecycle.serialize() if self.lifecycle else None,
            'bucket': self.bucket
        }

    @staticmethod
    def _validate_values(path, directory, acl):
        # type: (str, str, ACL) -> None

        if not (path or directory):
            raise ValueError('path or directory must be specified')

        FileDescriptor.acl_validator(acl)

        if path:
            FileDescriptor.path_validator(path)

        if directory:
            FileDescriptor.path_validator(directory)
