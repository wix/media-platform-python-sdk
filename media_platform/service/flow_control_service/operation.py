from media_platform.job.specification import Specification
from media_platform.lang.serialization import Serializable
from media_platform.service.file_descriptor import FileDescriptor
from media_platform.service.flow_control_service.component import Component, ComponentType
from media_platform.service.source import Source


class OperationStatus(object):
    waiting = 'waiting'
    aborted = 'aborted'
    working = 'working'
    success = 'success'
    error = 'error'


class Operation(Component):
    def __init__(self, component_type, specification, successors, status, delete_sources=False, sources=None,
                 results=None, jobs=None, extra_results=None, error_message=None, error_code=None):
        # type: (ComponentType, Specification, [str], OperationStatus, bool, [Source], [FileDescriptor] or [dict], [str], dict, str, int) -> None
        super(Operation, self).__init__(component_type, specification, successors, delete_sources)
        self.status = status
        self.sources = sources or []
        self.results = results or []
        self.jobs = jobs or []
        self.extra_results = extra_results or {}
        self.error_message = error_message
        self.error_code = error_code

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Operation
        component = super(Operation, cls).deserialize(data)

        sources_data = data.get('sources', [])
        results_data = data.get('results', [])

        sources = [Source.deserialize(s) for s in sources_data]
        results = [FileDescriptor.deserialize(r) for r in results_data]
        jobs = data.get('jobs', [])
        extra_results = data.get('extraResults', {})

        return Operation(component.type, component.specification, component.successors, data['status'],
                         component.delete_sources, sources, results, jobs, extra_results, data.get('errorMessage'),
                         data.get('errorCode'))

    def serialize(self):
        data = super(Operation, self).serialize()

        data.update({
            'sources': [s.serialize() for s in self.sources if s],
            'status': self.status,
            'results': [r.serialize() if isinstance(r, Serializable) else r for r in self.results],
            'jobs': self.jobs,
            'extraResults': self.extra_results
        })

        if self.error_code:
            data['errorCode'] = self.error_code

        if self.error_message:
            data['errorMessage'] = self.error_message

        return data
