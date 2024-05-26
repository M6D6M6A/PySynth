from enum import Enum, auto
import numpy as np


class CurveType(Enum):
    """
    Enum for different types of curves.
    """

    LINEAR = auto()
    EXPONENTIAL = auto()
    LOGARITHMIC = auto()
    SINE = auto()
    QUADRATIC = auto()
    CUBIC = auto()
    SIGMOID = auto()
    INVERSE_EXPONENTIAL = auto()
    TANH = auto()


class Curve:
    """
    A class to generate various curves.

    Attributes:
        sample_rate (int): The sample rate in Hz.
    """

    def __init__(self, sample_rate: int):
        """
        Initializes the Curve object with a sample rate.

        Args:
            sample_rate (int): The sample rate in Hz.
        """
        self.sample_rate = sample_rate

    def apply_curve(
        self, curve_type: CurveType, length: int, start: float = 0.0, end: float = 1.0
    ) -> np.ndarray:
        """
        Applies the specified curve to a range.

        Args:
            curve_type (CurveType): The type of curve to apply.
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated curve.
        """
        if curve_type == CurveType.LINEAR:
            return self.linear_curve(length, start, end)
        elif curve_type == CurveType.EXPONENTIAL:
            return self.exponential_curve(length, start, end)
        elif curve_type == CurveType.LOGARITHMIC:
            return self.logarithmic_curve(length, start, end)
        elif curve_type == CurveType.SINE:
            return self.sine_curve(length, start, end)
        elif curve_type == CurveType.QUADRATIC:
            return self.quadratic_curve(length, start, end)
        elif curve_type == CurveType.CUBIC:
            return self.cubic_curve(length, start, end)
        elif curve_type == CurveType.SIGMOID:
            return self.sigmoid_curve(length, start, end)
        elif curve_type == CurveType.INVERSE_EXPONENTIAL:
            return self.inverse_exponential_curve(length, start, end)
        elif curve_type == CurveType.TANH:
            return self.tanh_curve(length, start, end)
        else:
            raise ValueError("Unknown curve type")

    def linear_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a linear curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated linear curve.
        """
        return np.linspace(start, end, length)

    def exponential_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates an exponential curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated exponential curve.
        """
        return np.linspace(start, end, length) ** 2

    def logarithmic_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a logarithmic curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated logarithmic curve.
        """
        return np.logspace(np.log10(max(start, 1e-5)), np.log10(end), length)

    def sine_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a sine curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated sine curve.
        """
        return (
            start
            + (end - start)
            * (np.sin(np.linspace(-np.pi / 2, np.pi / 2, length)) + 1)
            / 2
        )

    def quadratic_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a quadratic curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated quadratic curve.
        """
        return (end - start) * (np.linspace(0, 1, length) ** 2) + start

    def cubic_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a cubic curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated cubic curve.
        """
        return (end - start) * (np.linspace(0, 1, length) ** 3) + start

    def sigmoid_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a sigmoid curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated sigmoid curve.
        """
        t = np.linspace(-6, 6, length)
        return start + (end - start) / (1 + np.exp(-t))

    def inverse_exponential_curve(
        self, length: int, start: float, end: float
    ) -> np.ndarray:
        """
        Generates an inverse exponential curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated inverse exponential curve.
        """
        return 1 - np.exp(-np.linspace(0, 5, length))

    def tanh_curve(self, length: int, start: float, end: float) -> np.ndarray:
        """
        Generates a hyperbolic tangent (tanh) curve.

        Args:
            length (int): The number of samples in the curve.
            start (float): The starting value of the curve.
            end (float): The ending value of the curve.

        Returns:
            np.ndarray: The generated tanh curve.
        """
        t = np.linspace(-3, 3, length)
        return start + (end - start) * (np.tanh(t) + 1) / 2
