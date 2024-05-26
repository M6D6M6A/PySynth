from .base_adsr_parameter import BaseADSRParameter
from ..curve import CurveType


class Attack(BaseADSRParameter):
    """
    A class to encapsulate the attack parameter.

    Attributes:
        value (float): The attack time in seconds.
        curve (CurveType): The curve type for the attack phase.
    """

    def __init__(self, value: float, curve: CurveType):
        """
        Initializes the Attack object.

        Args:
            value (float): The attack time in seconds. Should be positive.
            curve (CurveType): The curve type for the attack phase.
        """
        if value < 0:
            raise ValueError("Attack time must be positive.")
        super().__init__(value)
        self.curve = curve


class AttackPercent(BaseADSRParameter):
    """
    A class to encapsulate the attack parameter as a percentage of the total duration.

    Attributes:
        percent (float): The attack time as a percentage of the total duration.
        curve (CurveType): The curve type for the attack phase.
    """

    def __init__(self, percent: float, curve: CurveType):
        """
        Initializes the AttackPercent object.

        Args:
            percent (float): The attack time as a percentage of the total duration. Should be between 0 and 100.
            curve (CurveType): The curve type for the attack phase.
        """
        if not 0 <= percent <= 100:
            raise ValueError("Attack percent must be between 0 and 100.")
        super().__init__(percent)
        self.curve = curve

    def get_value(self, duration: float) -> float:
        """
        Returns the attack time as a fraction of the total duration.

        Args:
            duration (float): The duration of the sound.

        Returns:
            float: The attack time in seconds.
        """
        return (self.value / 100.0) * duration
