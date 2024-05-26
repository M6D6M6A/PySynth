from .base_adsr_parameter import BaseADSRParameter
from ..curve import CurveType


class Decay(BaseADSRParameter):
    """
    A class to encapsulate the decay parameter.

    Attributes:
        value (float): The decay time in seconds.
        curve (CurveType): The curve type for the decay phase.
    """

    def __init__(self, value: float, curve: CurveType):
        """
        Initializes the Decay object.

        Args:
            value (float): The decay time in seconds. Should be positive.
            curve (CurveType): The curve type for the decay phase.
        """
        if value < 0:
            raise ValueError("Decay time must be positive.")
        super().__init__(value)
        self.curve = curve


class DecayPercent(BaseADSRParameter):
    """
    A class to encapsulate the decay parameter as a percentage of the total duration.

    Attributes:
        percent (float): The decay time as a percentage of the total duration.
        curve (CurveType): The curve type for the decay phase.
    """

    def __init__(self, percent: float, curve: CurveType):
        """
        Initializes the DecayPercent object.

        Args:
            percent (float): The decay time as a percentage of the total duration. Should be between 0 and 100.
            curve (CurveType): The curve type for the decay phase.
        """
        if not 0 <= percent <= 100:
            raise ValueError("Decay percent must be between 0 and 100.")
        super().__init__(percent)
        self.curve = curve

    def get_value(self, duration: float) -> float:
        """
        Returns the decay time as a fraction of the total duration.

        Args:
            duration (float): The duration of the sound.

        Returns:
            float: The decay time in seconds.
        """
        return (self.value / 100.0) * duration
