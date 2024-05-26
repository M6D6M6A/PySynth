import py_synth


if __name__ == "__main__":
    sound = py_synth.Sound(
        waveform_type=py_synth.WaveformType.SAWTOOTH,
        frequency=py_synth.FullRangeFrequency(200.0),
        duration=2.0,
        envelope=py_synth.ADSREnvelope(
            attack=py_synth.AttackPercent(15, py_synth.CurveType.SINE),
            decay=py_synth.Decay(0.3, py_synth.CurveType.SINE),
            sustain=py_synth.Sustain(1.0),
            release=py_synth.Release(0.3),
            sustain_level=py_synth.SustainLevel(0.3),
        ),
    )

    synth = py_synth.Synthesizer(sample_rate=py_synth.SampleRate.CD_QUALITY)
    synth.play_sound(sound)
    
    synth.save_sound(sound, "output_sound", "wav")
