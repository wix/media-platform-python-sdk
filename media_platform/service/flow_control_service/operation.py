from __future__ import annotations

from typing import cast

from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.source import Source


class OperationStatus:
    waiting = 'waiting'
    aborted = 'aborted'
    working = 'working'
    success = 'success'
    error = 'error'


class Operation(Component):
    def __init__(self, component_type: ComponentType, successors: [str], specification: Specification,
                 status: OperationStatus, delete_sources: bool = False, sources: [Source] = None,
                 results: [FileDescriptor] or [dict] = None, jobs: [str] = None, extra_results: dict = None,
                 error_message: str = None, error_code: int = None, state_id: str = None, component_key: str = None):
        super().__init__(component_type, successors, specification, delete_sources, sources=sources)
        self.status = status
        self.results = results or []
        self.jobs = jobs or []
        self.extra_results = extra_results or {}
        self.error_message = error_message
        self.error_code = error_code
        self.state_id = state_id
        self.component_key = component_key

    @classmethod
    def deserialize(cls, data: dict) -> Operation:
        o = Component.deserialize(data)
        o.__class__ = cls

        o.status = data['status']
        o.results = [FileDescriptor.deserialize(r) for r in data.get('results', [])]
        o.jobs = data.get('jobs', [])
        o.extra_results = data.get('extraResults', {})
        o.error_message = data.get('errorMessage')
        o.error_code = data.get('errorCode')
        o.state_id = data.get('stateId')
        o.component_key = data.get('componentKey')
        return cast(Operation, o)

    def serialize(self) -> dict:
        data = super().serialize()

        data.update({
            'status': self.status,
            'results': [r.serialize() if isinstance(r, Serializable) else r for r in self.results],
            'jobs': self.jobs,
            'extraResults': self.extra_results
        })

        if self.error_code:
            data['errorCode'] = self.error_code

        if self.error_message:
            data['errorMessage'] = self.error_message

        if self.state_id:
            data['stateId'] = self.state_id

        if self.component_key:
            data['componentKey'] = self.component_key

        return data
