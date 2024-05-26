import numpy as np

from .base_adsr_parameter import BaseADSRParameter
from ..curve import Curve, CurveType


class ADSREnvelope:
    """
    A class to encapsulate ADSR (Attack, Decay, Sustain, Release) envelope options.

    Attributes:
        attack (Attack): The attack parameter.
        decay (Decay): The decay parameter.
        sustain (Sustain): The sustain parameter.
        release (Release): The release parameter.
        sustain_level (SustainLevel): The sustain level parameter.
    """

    def __init__(
        self,
        attack: BaseADSRParameter,
        decay: BaseADSRParameter,
        sustain: BaseADSRParameter,
        release: BaseADSRParameter,
        sustain_level: BaseADSRParameter,
    ):
        """
        Initializes the ADSREnvelope object with the specified parameters.

        Args:
            attack (BaseADSRParameter): The attack parameter.
            decay (BaseADSRParameter): The decay parameter.
            sustain (BaseADSRParameter): The sustain parameter.
            release (BaseADSRParameter): The release parameter.
            sustain_level (SustainLevel): The sustain level parameter.
        """
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.sustain_level = sustain_level

    def generate(self, sample_rate: int, duration: float) -> np.ndarray:
        """
        Generates an ADSR envelope.

        Args:
            sample_rate (int): The sample rate in Hz.
            duration (float): The duration of the sound in seconds.

        Returns:
            np.ndarray: The generated ADSR envelope.
        """
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        envelope_array = np.zeros_like(t)
        attack_samples = int(self.attack.get_value(duration) * sample_rate)
        decay_samples = int(self.decay.get_value(duration) * sample_rate)
        release_samples = int(self.release.get_value(duration) * sample_rate)
        sustain_samples = len(t) - attack_samples - decay_samples - release_samples

        curve = Curve(sample_rate)

        if attack_samples > 0:
            envelope_array[:attack_samples] = curve.apply_curve(
                self.attack.curve, attack_samples, start=0, end=1
            )

        if decay_samples > 0:
            envelope_array[attack_samples : attack_samples + decay_samples] = (
                curve.apply_curve(
                    self.decay.curve, decay_samples, start=1, end=self.sustain_level.value
                )
            )

        if sustain_samples > 0:
            envelope_array[
                attack_samples
                + decay_samples : attack_samples
                + decay_samples
                + sustain_samples
            ] = self.sustain_level.value

        if release_samples > 0:
            envelope_array[-release_samples:] = curve.apply_curve(
                CurveType.LINEAR, release_samples, start=self.sustain_level.value, end=0
            )

        return envelope_array
