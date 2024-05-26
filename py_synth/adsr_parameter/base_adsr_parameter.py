from ..curve import CurveType


class BaseADSRParameter:
    def __init__(self, value: float, curve: CurveType = CurveType.LINEAR):
        self.value = value
        self.curve = curve

    def get_value(self, duration: float) -> float:
        return self.value
