from .base_adsr_parameter import BaseADSRParameter
from ..curve import CurveType


class Sustain(BaseADSRParameter):
    """
    A class to encapsulate the sustain parameter.

    Attributes:
        value (float): The sustain time in seconds.
        curve (CurveType): The curve type for the sustain time.
    """

    def __init__(self, value: float, curve: CurveType = CurveType.LINEAR):
        """
        Initializes the Sustain object.

        Args:
            value (float): The sustain time in seconds. Should be positive.
            curve (CurveType): The curve type for the sustain time.
        """
        if value < 0:
            raise ValueError("Sustain time must be positive.")
        super().__init__(value, curve)


class SustainPercent(BaseADSRParameter):
    """
    A class to encapsulate the sustain parameter as a percentage of the total duration.

    Attributes:
        percent (float): The sustain time as a percentage of the total duration.
        curve (CurveType): The curve type for the sustain time.
    """

    def __init__(self, percent: float, curve: CurveType = CurveType.LINEAR):
        """
        Initializes the SustainPercent object.

        Args:
            percent (float): The sustain time as a percentage of the total duration. Should be between 0 and 100.
            curve (CurveType): The curve type for the sustain time.
        """
        if not 0 <= percent <= 100:
            raise ValueError("Sustain percent must be between 0 and 100.")
        super().__init__(percent, curve)

    def get_value(self, duration: float) -> float:
        """
        Returns the sustain time as a fraction of the total duration.

        Args:
            duration (float): The duration of the sound.

        Returns:
            float: The sustain time in seconds.
        """
        return (self.value / 100.0) * duration
