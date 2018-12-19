from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.file_descriptor import FileDescriptor, ACL
from media_platform.service.lifecycle import Lifecycle


class Destination(Serializable, Deserializable):
    def __init__(self, path=None, directory=None, acl=ACL.public, lifecycle=None):
        # type: (str, str or None, str, Lifecycle) -> None
        super(Destination, self).__init__()

        self._validate_values(path, directory, acl)

        self.path = path
        self.directory = directory
        self.acl = acl or ACL.public
        self.lifecycle = lifecycle

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Destination

        lifecycle_data = data.get('lifecycle')
        lifecycle = Lifecycle.deserialize(lifecycle_data) if lifecycle_data else None

        return cls(data.get('path'), data.get('directory'), data['acl'], lifecycle)

    def serialize(self):
        # type: () -> dict
        return {
            'path': self.path,
            'directory': self.directory,
            'acl': self.acl,
            'lifecycle': self.lifecycle.serialize() if self.lifecycle else None
        }

    @staticmethod
    def _validate_values(path, directory, acl):
        # type: (str, str, str) -> None

        if not (path or directory):
            raise ValueError('path or directory must be specified')

        FileDescriptor.acl_validator(acl)

        if path:
            FileDescriptor.path_validator(path)

        if directory:
            FileDescriptor.path_validator(directory)