from .base_adsr_parameter import BaseADSRParameter


class Release(BaseADSRParameter):
    """
    A class to encapsulate the release parameter.

    Attributes:
        value (float): The release time in seconds.
    """

    def __init__(self, value: float):
        """
        Initializes the Release object.

        Args:
            value (float): The release time in seconds. Should be positive.
        """
        if value < 0:
            raise ValueError("Release time must be positive.")
        super().__init__(value)


class ReleasePercent(BaseADSRParameter):
    """
    A class to encapsulate the release parameter as a percentage of the total duration.

    Attributes:
        percent (float): The release time as a percentage of the total duration.
    """

    def __init__(self, percent: float):
        """
        Initializes the ReleasePercent object.

        Args:
            percent (float): The release time as a percentage of the total duration. Should be between 0 and 100.
        """
        if not 0 <= percent <= 100:
            raise ValueError("Release percent must be between 0 and 100.")
        super().__init__(percent)

    def get_value(self, duration: float) -> float:
        """
        Returns the release time as a fraction of the total duration.

        Args:
            duration (float): The duration of the sound.

        Returns:
            float: The release time in seconds.
        """
        return (self.value / 100.0) * duration
