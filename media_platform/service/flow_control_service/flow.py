from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.flow_control_service.component import Component


class Flow(Serializable, Deserializable):
    def __init__(self, components=None):
        # type: ([str, Component]) -> None

        self.components = components or dict()

    def add_component(self, key, component):
        # type: (str, Component) -> Flow
        self.components[key] = component
        return self

    def validate(self):
        graph = self.components

        path = set()
        visited = set()

        def visit(key):

            if key in visited:
                return False

            visited.add(key)
            path.add(key)

            if graph.get(key):
                successors = graph.get(key).successors
                for successor in successors:
                    if successor in path or visit(successor):
                        return True

            path.remove(key)
            return False

        cyclic = any(visit(v) for v in graph)

        if cyclic:
            raise ValueError('cyclic dependency detected')

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> Flow

        components = dict()
        for key, value in data.items():
            components[key] = Component.deserialize(value)

        return Flow(components)

    def serialize(self):
        # type: () -> dict
        data = dict()
        for key, value in self.components.items():
            data[key] = value.serialize()

        return data
