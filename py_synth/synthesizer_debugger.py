from matplotlib import pyplot as plt
import numpy as np


class SynthesizerDebugger:
    """
    A class to handle debugging by plotting and printing samples.

    Attributes:
        t (np.ndarray): The time array for the duration of the waveform.
    """

    def __init__(self, t: np.ndarray):
        """
        Initializes the Debugger object with a time array.

        Args:
            t (np.ndarray): The time array for the duration of the waveform.
        """
        self.t = t

    def plot_waveform(
        self, waveform: np.ndarray, envelope: np.ndarray, audio: np.ndarray
    ):
        """
        Plots the waveform, ADSR envelope, and output audio.

        Args:
            waveform (np.ndarray): The generated waveform.
            envelope (np.ndarray): The ADSR envelope applied to the waveform.
            audio (np.ndarray): The final audio signal.
        """
        plt.figure(figsize=(15, 5))

        plt.subplot(3, 1, 1)
        plt.plot(self.t, waveform, label="Waveform")
        plt.title("Waveform")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.t, envelope, label="ADSR Envelope", color="orange")
        plt.title("ADSR Envelope")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.t, audio, label="Output Audio", color="green")
        plt.title("Output Audio")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.tight_layout()
        plt.show()

    def print_samples(
        self,
        waveform: np.ndarray,
        envelope: np.ndarray,
        audio: np.ndarray,
        sample_rate: int = 100,
    ):
        """
        Prints samples of the waveform, envelope, and audio at regular intervals.

        Args:
            waveform (np.ndarray): The generated waveform.
            envelope (np.ndarray): The ADSR envelope applied to the waveform.
            audio (np.ndarray): The final audio signal.
            sample_rate (int): The rate at which samples are printed.
        """
        sample_indices = np.arange(0, len(self.t), int(len(self.t) / sample_rate))
        print("Samples at regular intervals:")
        print(
            f"{'Index':>6} {'Time':>10} {'Waveform':>10} {'Envelope':>10} {'Audio':>10}"
        )
        for i in sample_indices:
            print(
                f"{i:>6} {self.t[i]:>10.4f} {waveform[i]:>10.4f} {envelope[i]:>10.4f} {audio[i]:>10.4f}"
            )
