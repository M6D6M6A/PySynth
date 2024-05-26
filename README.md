# PySynth

PySynth is a Python-based synthesizer for generating and manipulating sound waves. This repository contains the core components for creating and playing sounds using various waveform types and applying ADSR (Attack, Decay, Sustain, Release) envelopes. The project is designed to be easily extendable and customizable for different sound synthesis needs.

## Features

-   **Waveform Generation**: Supports multiple waveform types such as Sine, Square, Triangle, and Pulse.
-   **ADSR Envelope**: Implements a flexible ADSR envelope to shape the amplitude of the sound over time.
-   **Curve Types**: Provides various curve types for smoother transitions in the ADSR envelope.
-   **Sample Rates**: Configurable sample rates to control the quality and size of the generated audio.
-   **Simple API**: Easy-to-use interface for creating and playing sounds.

## Installation

To get started with PySynth, clone the repository and install the required dependencies:

```bash
git clone https://github.com/M6D6M6A/PySynth.git
cd PySynth
pip install -r requirements.txt
```

## Usage

Here's a basic example of how to use PySynth to create and play a sound:

```python
envelope = py_synth.ADSREnvelope(
    attack=py_synth.AttackPercent(40, py_synth.CurveType.SINE),
    decay=py_synth.DecayPercent(30, py_synth.CurveType.SINE),
    sustain=py_synth.SustainPercent(20),
    sustain_level=py_synth.SustainLevel(0.7),
    release=py_synth.ReleasePercent(10, py_synth.CurveType.SINE),
)

# Define the sound parameters
sound = py_synth.Sound(
    waveform_type=py_synth.WaveformType.PULSE,
    frequency=py_synth.FullRangeFrequency(440.0),
    duration=2.0,
    envelope=envelope,
)

synth = py_synth.Synthesizer(sample_rate=py_synth.SampleRate.CD_QUALITY)
synth.play_sound(sound)

synth.save_sound(sound, "output_sound", "wav")
```

## Curve Types

PySynth supports various curve types for more natural transitions in the ADSR envelope:

-   **LINEAR**: Straight line interpolation.
-   **EXPONENTIAL**: Exponential growth.
-   **LOGARITHMIC**: Logarithmic curve.
-   **SINE**: Sine wave.
-   **QUADRATIC**: Quadratic curve.
-   **CUBIC**: Cubic curve.
-   **SIGMOID**: Sigmoid function.
-   **INVERSE_EXPONENTIAL**: Inverse exponential.
-   **TANH**: Hyperbolic tangent.
