import numpy as np
from .base_adsr_parameter import BaseADSRParameter
from ..curve import Curve

class ADSREnvelope:
    """
    A class to encapsulate ADSR (Attack, Decay, Sustain, Release) envelope options.

    Attributes:
        attack (BaseADSRParameter): The attack parameter.
        decay (BaseADSRParameter): The decay parameter.
        sustain (BaseADSRParameter): The sustain parameter.
        release (BaseADSRParameter): The release parameter.
        sustain_level (BaseADSRParameter): The sustain level parameter.
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
            sustain_level (BaseADSRParameter): The sustain level parameter.
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
        num_samples = int(sample_rate * duration)
        envelope_array = np.zeros(num_samples)
        
        attack_samples = int(self.attack.get_value(duration) * sample_rate)
        decay_samples = int(self.decay.get_value(duration) * sample_rate)
        sustain_samples = int(self.sustain.get_value(duration) * sample_rate)
        release_samples = int(self.release.get_value(duration) * sample_rate)

        curve = Curve(sample_rate)

        current_position = 0

        if attack_samples > 0:
            envelope_array[:attack_samples] = curve.apply_curve(
                self.attack.curve, attack_samples, start=0, end=1
            )
            current_position += attack_samples

        if decay_samples > 0:
            envelope_array[current_position:current_position + decay_samples] = (
                curve.apply_curve(
                    self.decay.curve,
                    decay_samples,
                    start=1,
                    end=self.sustain_level.get_value(duration),
                )
            )
            current_position += decay_samples

        if sustain_samples > 0:
            envelope_array[current_position:current_position + sustain_samples] = self.sustain_level.get_value(duration)
            current_position += sustain_samples

        if release_samples > 0:
            envelope_array[-release_samples:] = curve.apply_curve(
                self.release.curve,
                release_samples,
                start=self.sustain_level.get_value(duration),
                end=0,
            )

        return envelope_array
