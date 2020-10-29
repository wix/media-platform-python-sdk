from abc import ABC, abstractmethod


class Serializable(ABC):

    @abstractmethod
    def serialize(self) -> dict:
        pass


class Deserializable(ABC):

    @classmethod
    @abstractmethod
    def deserialize(cls, data: dict):
        pass
