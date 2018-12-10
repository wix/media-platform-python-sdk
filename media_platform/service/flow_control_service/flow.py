import copy

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
        # don't mess with the original
        remaining_components = copy.copy(self.components)

        while remaining_components:
            acyclic = False

            for key, component in remaining_components.items():
                for successor in component.successors:
                    if successor not in self.components:
                        raise ValueError('undefined dependency detected: %s' % successor)

                    if successor in remaining_components:
                        break
                else:
                    acyclic = True
                    del remaining_components[key]

            if not acyclic:
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
