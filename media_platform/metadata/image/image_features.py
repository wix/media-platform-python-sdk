from __future__ import annotations

from media_platform.lang.serialization import Deserializable
from media_platform.metadata.features.crop_hint import CropHint
from media_platform.metadata.features.explicit_content import ExplicitContent
from media_platform.metadata.features.image_color import Color
from media_platform.metadata.features.label import Label
from media_platform.metadata.features.rectangle import Rectangle


class ImageFeatures(Deserializable):
    def __init__(self, labels: [Label] = None, faces: [Rectangle] = None, colors: [Color] = None,
                 explicit_content: [ExplicitContent] = None, crop_hints: [CropHint] = None):
        self.labels = labels or []
        self.faces = faces or []
        self.colors = colors or []
        self.explicit_content = explicit_content or []
        self.crop_hints = crop_hints or []

    @classmethod
    def deserialize(cls, data: dict) -> ImageFeatures:
        labels = [Label.deserialize(label) for label in data.get('labels', [])]
        faces = [Rectangle.deserialize(face) for face in data.get('faces', [])]
        colors = [Color.deserialize(color) for color in data.get('colors', [])]
        explicit_content = [ExplicitContent.deserialize(content) for content in data.get('explicitContent', [])]
        crop_hints = [CropHint.deserialize(content) for content in data.get('cropHints', [])]

        return ImageFeatures(labels, faces, colors, explicit_content, crop_hints)
