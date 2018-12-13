from media_platform.lang.serialization import Deserializable
from media_platform.metadata.features.explicit_content import ExplicitContent
from media_platform.metadata.features.image_color import Color
from media_platform.metadata.features.label import Label
from media_platform.metadata.features.rectangle import Rectangle


class ImageFeatures(Deserializable):
    def __init__(self, labels=None, faces=None, colors=None, explicit_content=None):
        # type: ([Label], [Rectangle], [Color], [ExplicitContent]) -> None
        self.labels = labels or []
        self.faces = faces or []
        self.colors = colors or []
        self.explicit_content = explicit_content or []

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageFeatures
        labels = [Label.deserialize(label) for label in data.get('labels', [])]
        faces = [Rectangle.deserialize(face) for face in data.get('faces', [])]
        colors = [Color.deserialize(color) for color in data.get('colors', [])]
        explicit_content = [ExplicitContent.deserialize(content) for content in data.get('explicitContent', [])]

        return ImageFeatures(labels, faces, colors, explicit_content)
