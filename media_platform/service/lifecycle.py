from media_platform.lang.serializable import Serializable


class Action(object):
    delete = 'delete'

    @classmethod
    def has_value(cls, value):
        return value in [cls.delete]


class Lifecycle(Serializable):
    def __init__(self, age, action):
        # type: (int, str) -> None
        super(Lifecycle, self).__init__()

        if age < 30:
            raise ValueError('age must be greater than 30 seconds')

        if age > 365 * 24 * 60 * 60:
            raise ValueError('age must be less than 365 days')

        if not Action.has_value(action):
            raise ValueError('action %s not supported' % action)

        self.age = age          # int seconds
        self.action = action    # delete

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Lifecycle

        return Lifecycle(data['age'], data['action'])

    def serialize(self):
        return {
            'age': self.age,
            'action': self.action
        }
