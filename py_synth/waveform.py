import numpy as np
from enum import Enum, auto


class WaveformType(Enum):
    """
    Enum for different types of waveforms.
    """

    SINE = auto()
    SQUARE = auto()
    SAWTOOTH = auto()
    TRIANGLE = auto()
    PULSE = auto()
    NOISE = auto()


class Waveform:
    """
    A class to generate various waveforms.

    Attributes:
        sample_rate (int): The sample rate in Hz.
        duration (float): The duration of the waveform in seconds.
        t (np.ndarray): The time array for the duration of the waveform.
    """

    def __init__(self, sample_rate=44100, duration=2.0):
        """
        Initializes the Waveform object with a sample rate and duration.

        Args:
            sample_rate (int): The sample rate in Hz.
            duration (float): The duration of the waveform in seconds.
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    def generate(self, waveform_type: WaveformType, frequency: float, num_samples: int) -> np.ndarray:
        """
        Generates the specified waveform.

        Args:
            waveform_type (WaveformType): The type of waveform to generate.
            frequency (float): The frequency of the waveform in Hz.

        Returns:
            np.ndarray: The generated waveform.
        """
        t = np.linspace(0, num_samples / self.sample_rate, num_samples, endpoint=False)
        if waveform_type == WaveformType.SINE:
            return np.sin(2 * np.pi * frequency * t)
        elif waveform_type == WaveformType.SQUARE:
            return np.sign(np.sin(2 * np.pi * frequency * t))
        elif waveform_type == WaveformType.SAWTOOTH:
            return 2 * (t * frequency - np.floor(0.5 + t * frequency))
        elif waveform_type == WaveformType.TRIANGLE:
            return 2 * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5))) - 1
        elif waveform_type == WaveformType.PULSE:
            return np.where(np.mod(t * frequency, 1) < 0.5, 1.0, -1.0)
        elif waveform_type == WaveformType.NOISE:
            return np.random.uniform(-1.0, 1.0, len(t))
        else:
            raise ValueError("Unknown waveform type")

    def sine_wave(self, frequency: float) -> np.ndarray:
        """
        Generates a sine wave.

        Args:
            frequency (float): The frequency of the sine wave in Hz.

        Returns:
            np.ndarray: The generated sine wave.
        """
        return np.sin(2 * np.pi * frequency * self.t)

    def square_wave(self, frequency: float) -> np.ndarray:
        """
        Generates a square wave.

        Args:
            frequency (float): The frequency of the square wave in Hz.

        Returns:
            np.ndarray: The generated square wave.
        """
        return np.sign(np.sin(2 * np.pi * frequency * self.t))

    def sawtooth_wave(self, frequency: float) -> np.ndarray:
        """
        Generates a sawtooth wave.

        Args:
            frequency (float): The frequency of the sawtooth wave in Hz.

        Returns:
            np.ndarray: The generated sawtooth wave.
        """
        return 2 * (self.t * frequency - np.floor(0.5 + self.t * frequency))

    def triangle_wave(self, frequency: float) -> np.ndarray:
        """
        Generates a triangle wave.

        Args:
            frequency (float): The frequency of the triangle wave in Hz.

        Returns:
            np.ndarray: The generated triangle wave.
        """
        return (
            2 * np.abs(2 * (self.t * frequency - np.floor(self.t * frequency + 0.5)))
            - 1
        )

    def pulse_wave(self, frequency: float, duty_cycle: float = 0.5) -> np.ndarray:
        """
        Generates a pulse wave.

        Args:
            frequency (float): The frequency of the pulse wave in Hz.
            duty_cycle (float): The duty cycle of the pulse wave (0.0 to 1.0).

        Returns:
            np.ndarray: The generated pulse wave.
        """
        return np.where(np.mod(self.t * frequency, 1) < duty_cycle, 1.0, -1.0)

    def noise_wave(self) -> np.ndarray:
        """
        Generates white noise.

        Returns:
            np.ndarray: The generated white noise.
        """
        return np.random.uniform(-1.0, 1.0, len(self.t))
