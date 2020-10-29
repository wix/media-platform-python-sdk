from __future__ import annotations

from media_platform.lang.serialization import Serializable, Deserializable


class Action:
    delete = 'delete'

    @classmethod
    def has_value(cls, value):
        return value in [cls.delete]


class Lifecycle(Serializable, Deserializable):
    def __init__(self, age: int, action: Action):
        self._validate_values(action, age)
        self.age = age  # int seconds
        self.action = action  # delete

    @classmethod
    def deserialize(cls, data: dict) -> Lifecycle:
        return Lifecycle(data['age'], data['action'])

    def serialize(self) -> dict:
        return {
            'age': self.age,
            'action': self.action
        }

    @staticmethod
    def _validate_values(action: Action, age: int):
        if age < 30:
            raise ValueError('age must be greater than 30 seconds')

        if age > 365 * 24 * 60 * 60:
            raise ValueError('age must be less than 365 days')

        if not Action.has_value(action):
            raise ValueError('action %s not supported' % action)
