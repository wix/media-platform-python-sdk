from __future__ import annotations

from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.flow_control_service.component import ComponentType


class FlowError(Deserializable, Serializable):
    def __init__(self, component_type: ComponentType, component_key: str, message: str = None):
        self.component_type = component_type
        self.component_key = component_key
        self.message = message

    @classmethod
    def deserialize(cls, data: dict) -> FlowError:
        return FlowError(data['componentType'], data['componentKey'], data.get('message'))

    def serialize(self) -> dict:
        return {
            'componentType': self.component_type,
            'componentKey': self.component_key,
            'message': self.message
        }
