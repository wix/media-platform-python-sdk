from media_platform.lang.serialization import Deserializable
from media_platform.service.flow_control_service.component import ComponentType


class FlowError(Deserializable):
    def __init__(self, component_type, component_key, message=None):
        # type: (ComponentType, str, str) -> None
        super(FlowError, self).__init__()
        self.component_type = component_type
        self.component_key = component_key
        self.message = message

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FlowError

        return FlowError(data['componentType'], data['componentKey'], data.get('message'))

    def serialize(self):
        return {
            'componentType': self.component_type,
            'componentKey': self.component_key,
            'message': self.message
        }