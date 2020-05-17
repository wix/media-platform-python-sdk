from media_platform.metadata.features.rectangle import Rectangle


class CropHint(Rectangle):
    def __init__(self, x, y, width, height, confidence, importance_fraction):
        # type: (int, int, int, int, float, float) -> None
        super(CropHint, self).__init__(x, y, width, height)
        self.confidence = confidence
        self.importance_fraction = importance_fraction

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> CropHint
        return CropHint(data['x'], data['y'], data['width'], data['height'], data['confidence'],
                        data['importanceFraction'])
