from abc import ABC, abstractmethod

from media_platform.lang.serialization import Serializable, Deserializable


class Specification(Serializable, Deserializable, ABC):

    @abstractmethod
    def serialize(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, data):
        pass

    # override for request pre-flight check
    def validate(self):
        pass
