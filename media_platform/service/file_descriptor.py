from datetime import datetime

from media_platform.lang import datetime_serialization
from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.lifecycle import Lifecycle


class ACL(object):
    public = 'public'
    private = 'private'

    @classmethod
    def has_value(cls, value):
        return value in [cls.public, cls.private]


class FileType(object):
    file = '-'
    directory = 'd'
    symlink = 'l'


class FileMimeType(object):
    directory = 'application/vnd.wix-media.dir'
    symlink = 'application/vnd.wix-media.symlink'

    defualt = 'application/octet-stream'


class FileDescriptor(Serializable, Deserializable):
    def __init__(self, path, file_id, file_type, mime_type, size, acl=ACL.public, lifecycle=None, file_hash=None,
                 date_created=None, date_updated=None):
        # type: (str, str, str, str, int, ACL, Lifecycle, str, datetime, datetime) -> None
        super(FileDescriptor, self).__init__()

        self._validate_values(acl, path)

        self.path = path
        self.id = file_id
        self.type = file_type
        self.mime_type = mime_type
        self.size = size
        self.acl = acl
        self.lifecycle = lifecycle
        self.hash = file_hash
        self.date_created = date_created or datetime.utcnow()
        self.date_updated = date_updated or datetime.utcnow()

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FileDescriptor

        lifecycle_data = data.get('lifecycle')
        lifecycle = Lifecycle.deserialize(lifecycle_data) if lifecycle_data else None

        return FileDescriptor(data['path'], data['id'], data['type'], data['mimeType'], data['size'], data['acl'],
                              lifecycle, data.get('hash'),
                              datetime_serialization.deserialize(data.get('dateCreated')),
                              datetime_serialization.deserialize(data.get('dateUpdated')))

    def serialize(self):
        # type: () -> dict
        return {
            'id': self.id,
            'path': self.path,
            'type': self.type,
            'mimeType': self.mime_type,
            'size': self.size,
            'hash': self.hash,
            'acl': self.acl,
            'lifecycle': self.lifecycle.serialize() if self.lifecycle else None,
            'dateUpdated': datetime_serialization.serialize(self.date_updated),
            'dateCreated': datetime_serialization.serialize(self.date_created)
        }

    @staticmethod
    def _validate_values(acl, path):
        FileDescriptor.path_validator(path)
        FileDescriptor.acl_validator(acl)

    @staticmethod
    def path_validator(path):
        # type: (str) -> None
        if not path.startswith('/'):
            raise ValueError('path must start with "/"' % path)

    @staticmethod
    def acl_validator(acl):
        if not ACL.has_value(acl):
            raise ValueError('ACL %s not supported' % acl)
