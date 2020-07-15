from __future__ import annotations

import re

from media_platform.lang.serialization import Serializable, Deserializable
from media_platform.service.flow_control_service.component import Component


class Flow(Serializable, Deserializable):
    def __init__(self, components: [str, Component] = None):
        self.components = components or dict()

    def add_component(self, key: str, component: Component) -> Flow:
        self.components[key] = component
        return self

    def validate(self):
        self._validate_keys()
        self._validate_successors()
        self._validate_acyclic()

    @classmethod
    def deserialize(cls, data: dict) -> Flow:
        components = {k: Component.deserialize(v) for k, v in data.items()}

        return Flow(components)

    def serialize(self) -> dict:
        return {k: v.serialize() for k, v in self.components.items()}

    _invalid_key_chars = re.compile('[^A-Za-z0-9-]')

    def _validate_keys(self):
        for k in self.components.keys():
            if re.search(self._invalid_key_chars, k):
                raise ValueError('Component keys must contain only uppercase and lowercase letters, digits and hyphens')

    def _validate_successors(self):
        missing_successors = [s for c in self.components.values() for s in c.successors if s not in self.components]
        if missing_successors:
            raise ValueError('Missing successor components: %s' % missing_successors)

    def _validate_acyclic(self):
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

        if any(visit(v) for v in graph):
            raise ValueError('cyclic dependency detected')
