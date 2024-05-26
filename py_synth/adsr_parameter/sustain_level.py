from .base_adsr_parameter import BaseADSRParameter
from ..curve import CurveType


class SustainLevel(BaseADSRParameter):
    """
    A class to encapsulate the sustain level parameter.

    Attributes:
        value (float): The sustain level.
        curve (CurveType): The curve type for the sustain level.
    """

    def __init__(self, value: float, curve: CurveType = CurveType.LINEAR):
        """
        Initializes the SustainLevel object.

        Args:
            value (float): The sustain level. Typically between 0.0 (silence) and 1.0 (full volume).
            curve (CurveType): The curve type for the sustain level.
        """
        if not 0.0 <= value <= 1.0:
            raise ValueError("Sustain level must be between 0.0 and 1.0.")
        super().__init__(value, curve)
