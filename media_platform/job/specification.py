from abc import ABC

from media_platform.lang.serialization import Serializable, Deserializable


class Specification(ABC, Serializable, Deserializable):

    def serialize(self):
        raise NotImplementedError()

    @classmethod
    def deserialize(cls, data):
        raise NotImplementedError()

    # override for request pre-flight check
    def validate(self):
        pass
