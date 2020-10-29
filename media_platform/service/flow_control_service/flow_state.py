from __future__ import annotations

from media_platform.lang.serialization import Deserializable, Serializable
from media_platform.service.flow_control_service.flow_error import FlowError
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.flow_control_service.operation import Operation


class FlowStatus:
    idle = 'idle'
    working = 'working'
    success = 'success'
    error = 'error'
    aborted = 'aborted'


class FlowState(Deserializable, Serializable):
    def __init__(self, flow_id: str, status: FlowStatus, invocation: Invocation, operations: [str, Operation],
                 flow_error: FlowError = None):
        self.id = flow_id
        self.invocation = invocation
        self.operations = operations
        self.status = status
        self.flow_error = flow_error

    @classmethod
    def deserialize(cls, data: dict) -> FlowState:
        invocation = Invocation.deserialize(data['invocation'])
        operations_data = data.get('operations', {})
        operations = {k: Operation.deserialize(v) for k, v in operations_data.items()}
        flow_error_data = data.get('error')
        flow_error = FlowError.deserialize(flow_error_data) if flow_error_data else None

        return FlowState(data['id'], data['status'], invocation, operations, flow_error)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'invocation': self.invocation.serialize(),
            'operations': {k: v.serialize() for k, v in self.operations.items()},
            'status': self.status,
            'error': self.flow_error.serialize() if self.flow_error else None
        }
