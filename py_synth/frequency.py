class BaseFrequency:
    """
    A base class to encapsulate frequency options.

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the BaseFrequency object.

        Args:
            value (float): The frequency value in Hz.
        """
        self.value = value


class CommonFrequency(BaseFrequency):
    """
    A class to encapsulate common frequency options. (20 Hz to 20000 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the CommonFrequency object.

        Args:
            value (float): The frequency value in Hz. Typical range for a synth is from 20 Hz to 20000 Hz.
        """
        if not 20 <= value <= 20000:
            raise ValueError("Frequency must be between 20 Hz and 20000 Hz.")
        super().__init__(value)


class FullRangeFrequency(BaseFrequency):
    """
    A class to encapsulate full-range frequency options. (0 Hz to 40000 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the FullRangeFrequency object.

        Args:
            value (float): The frequency value in Hz. Full range for a synth is from 0 Hz to 40000 Hz.
        """
        if not 0 <= value <= 40000:
            raise ValueError("Frequency must be between 0 Hz and 40000 Hz.")
        super().__init__(value)


class SubsonicFrequency(BaseFrequency):
    """
    A class to encapsulate subsonic frequency options. (0 Hz and 20 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the SubsonicFrequency object.

        Args:
            value (float): The frequency value in Hz. Subsonic range is from 0 Hz to 20 Hz.
        """
        if not 0 <= value <= 20:
            raise ValueError("Frequency must be between 0 Hz and 20 Hz.")
        super().__init__(value)


class UltrasonicFrequency(BaseFrequency):
    """
    A class to encapsulate ultrasonic frequency options. (20000 Hz to 40000 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the UltrasonicFrequency object.

        Args:
            value (float): The frequency value in Hz. Ultrasonic range is from 20000 Hz to 40000 Hz.
        """
        if not 20000 <= value <= 40000:
            raise ValueError("Frequency must be between 20000 Hz and 40000 Hz.")
        super().__init__(value)


class InaudibleLowFrequency(SubsonicFrequency):
    """
    A class to encapsulate inaudible low frequency options (subsonic, 0 Hz and 20 Hz).

    Attributes:
        value (float): The frequency value in Hz.
    """


class InaudibleHighFrequency(UltrasonicFrequency):
    """
    A class to encapsulate inaudible high frequency options (ultrasonic, 20000 Hz to 40000 Hz).

    Attributes:
        value (float): The frequency value in Hz.
    """


class BassFrequency(BaseFrequency):
    """
    A class to encapsulate bass frequency options. (20 Hz to 250 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the BassFrequency object.

        Args:
            value (float): The frequency value in Hz. Bass range is from 20 Hz to 250 Hz.
        """
        if not 20 <= value <= 250:
            raise ValueError("Frequency must be between 20 Hz and 250 Hz.")
        super().__init__(value)


class LowFrequency(BaseFrequency):
    """
    A class to encapsulate low frequency options. (20 Hz to 500 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the LowFrequency object.

        Args:
            value (float): The frequency value in Hz. Low range is from 20 Hz to 500 Hz.
        """
        if not 20 <= value <= 500:
            raise ValueError("Frequency must be between 20 Hz and 500 Hz.")
        super().__init__(value)


class MidFrequency(BaseFrequency):
    """
    A class to encapsulate mid frequency options. (250 Hz to 4000 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the MidFrequency object.

        Args:
            value (float): The frequency value in Hz. Mid range is from 250 Hz to 4000 Hz.
        """
        if not 250 <= value <= 4000:
            raise ValueError("Frequency must be between 250 Hz and 4000 Hz.")
        super().__init__(value)


class HighFrequency(BaseFrequency):
    """
    A class to encapsulate high frequency options. (4000 Hz to 20000 Hz)

    Attributes:
        value (float): The frequency value in Hz.
    """

    def __init__(self, value: float):
        """
        Initializes the HighFrequency object.

        Args:
            value (float): The frequency value in Hz. High range is from 4000 Hz to 20000 Hz.
        """
        if not 4000 <= value <= 20000:
            raise ValueError("Frequency must be between 4000 Hz and 20000 Hz.")
        super().__init__(value)
