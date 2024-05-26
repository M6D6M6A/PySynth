class BaseADSRParameter:
    """
    A base class for ADSR (Attack, Decay, Sustain, Release) parameters.

    Attributes:
        value (float): The time or level value.
    """

    def __init__(self, value: float):
        """
        Initializes the BaseADSRParameter object.

        Args:
            value (float): The time or level value.
        """
        self.value = value

    def get_value(self, duration: float) -> float:
        """
        Returns the parameter value, potentially adjusted by duration.

        Args:
            duration (float): The duration of the sound.

        Returns:
            float: The adjusted parameter value.
        """
        return self.value
