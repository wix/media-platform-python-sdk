from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.file_descriptor import FileDescriptor, ACL
from media_platform.service.lifecycle import Lifecycle


class Destination(Serializable, Deserializable):
    def __init__(self, path: str = None, directory: str = None, acl: ACL = ACL.public, lifecycle: Lifecycle = None,
                 bucket: str = None):
        self._validate_values(path, directory, acl)

        self.path = path
        self.directory = directory
        self.acl = acl or ACL.public
        self.lifecycle = lifecycle
        self.bucket = bucket

    @classmethod
    def deserialize(cls, data: dict) -> Destination:
        lifecycle_data = data.get('lifecycle')
        lifecycle = Lifecycle.deserialize(lifecycle_data) if lifecycle_data else None

        return cls(data.get('path'), data.get('directory'), data['acl'], lifecycle, data.get('bucket'))

    def serialize(self):
        return {
            'path': self.path,
            'directory': self.directory,
            'acl': self.acl,
            'lifecycle': self.lifecycle.serialize() if self.lifecycle else None,
            'bucket': self.bucket
        }

    @staticmethod
    def _validate_values(path: str, directory: str, acl: ACL):
        if not (path or directory):
            raise ValueError('path or directory must be specified')

        FileDescriptor.acl_validator(acl)

        if path:
            FileDescriptor.path_validator(path)

        if directory:
            FileDescriptor.path_validator(directory)
