from pathlib import Path
import numpy as np
import sounddevice as sd
import soundfile as sf

from .sound import SampleRate, Sound
from .waveform import Waveform
from .synthesizer_debugger import SynthesizerDebugger


class Synthesizer:
    """
    A class to synthesize audio using waveforms and ADSR envelopes.

    Attributes:
        sample_rate (int): The sample rate in Hz.
        waveform (Waveform): The waveform generator object.
        debugger (Debugger): The debugger object for plotting and printing samples.
    """

    _DIR = Path(__file__).resolve().parent
    _FILES_DIR = _DIR.parent / "files"

    def __init__(
        self, sample_rate: SampleRate = SampleRate.CD_QUALITY, show=True, debug=False
    ):
        """
        Initializes the Synthesizer object with a sample rate.

        Args:
            sample_rate (SampleRate): The sample rate in Hz.
        """
        self.show = show
        self.debug = debug
        self.sample_rate = sample_rate.value
        self.waveform = Waveform(self.sample_rate)
        self.debugger = None

        self._FILES_DIR.mkdir(exist_ok=True, parents=True)

    def set_debugger(self, sound: Sound):
        """
        Sets the debugger object for plotting and printing samples based on the sound duration.

        Args:
            sound (Sound): The sound object containing the duration.
        """
        t = np.linspace(
            0, sound.duration, int(self.sample_rate * sound.duration), endpoint=False
        )
        self.debugger = SynthesizerDebugger(t)

    def play_sound(self, sound: Sound):
        """
        Generates and plays a sound using the specified parameters.

        Args:
            sound (Sound): The sound parameters encapsulated in a Sound object.
        """
        if self.debug or self.show:
            self.set_debugger(sound)

        num_samples = int(self.sample_rate * sound.duration)
        waveform = self.waveform.generate(
            sound.waveform_type, sound.frequency.value, num_samples
        )
        envelope = sound.envelope.generate(self.sample_rate, sound.duration)
        audio = 0.5 * waveform * envelope

        if self.debug:
            self.debugger.print_samples(waveform, envelope, audio, sample_rate=100)

        sd.play(audio, self.sample_rate)
        sd.wait()

        if self.show:
            self.debugger.plot_waveform(waveform, envelope, audio)

    def save_sound(self, sound: Sound, filename: str, file_format: str):
        """
        Generates and saves a sound to a file in the specified format.

        Args:
            sound (Sound): The sound parameters encapsulated in a Sound object.
            filename (str): The name of the file to save the sound.
            file_format (str): The format to save the sound file in (e.g., 'wav', 'flac', 'ogg').
        """
        num_samples = int(self.sample_rate * sound.duration)
        waveform = self.waveform.generate(
            sound.waveform_type, sound.frequency.value, num_samples
        )
        envelope = sound.envelope.generate(self.sample_rate, sound.duration)
        audio = 0.5 * waveform * envelope

        sf.write(
            self._FILES_DIR / f"{filename}.{file_format}",
            audio,
            self.sample_rate,
            format=file_format.upper(),
        )
