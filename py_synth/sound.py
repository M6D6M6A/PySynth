from enum import Enum

from .waveform import WaveformType
from .frequency import BaseFrequency
from .adsr_parameter import ADSREnvelope


class SampleRate(Enum):
    """
    Enum for different sample rates.
    """

    LOW = 8000
    CD_QUALITY = 44100
    DVD_QUALITY = 48000
    STUDIO_QUALITY = 96000
    HIGH_RESOLUTION = 192000


class Sound:
    """
    A class to encapsulate all options to modify the sound.

    Attributes:
        waveform_type (WaveformType): The type of waveform to generate.
        frequency (BaseFrequency): The frequency of the waveform.
        duration (float): The duration of the sound in seconds.
        envelope (ADSREnvelope): The ADSR envelope options.
    """

    def __init__(
        self,
        waveform_type: WaveformType,
        frequency: BaseFrequency,
        duration: float,
        envelope: ADSREnvelope,
    ):
        """
        Initializes the Sound object with the specified parameters.

        Args:
            waveform_type (WaveformType): The type of waveform to generate.
            frequency (BaseFrequency): The frequency of the waveform.
            duration (float): The duration of the sound in seconds. Should be positive.
            envelope (ADSREnvelope): The ADSR envelope options.
        """
        if duration <= 0:
            raise ValueError("Duration must be positive.")

        self.waveform_type = waveform_type
        self.frequency = frequency
        self.duration = duration
        self.envelope = envelope
