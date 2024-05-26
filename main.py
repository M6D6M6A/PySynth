import py_synth


if __name__ == "__main__":
    # Define the ADSR envelope parameters
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
