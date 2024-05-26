import py_synth


def create_kick():
    duration = 0.5  # Duration in seconds

    envelope = py_synth.ADSREnvelope(
        attack=py_synth.AttackPercent(10, py_synth.CurveType.SINE),
        decay=py_synth.DecayPercent(20, py_synth.CurveType.SINE),
        sustain_level=py_synth.SustainLevel(0.7),
        sustain=py_synth.SustainPercent(50),
        release=py_synth.ReleasePercent(20, py_synth.CurveType.SINE),
    )

    sound = py_synth.Sound(
        waveform_type=py_synth.WaveformType.SINE,
        frequency=py_synth.BaseFrequency(60.0),  # py_synth.Notes.C3
        duration=duration,
        envelope=envelope,
    )
    return sound


if __name__ == "__main__":
    sample_rate = py_synth.SampleRate.HIGH_RESOLUTION
    synth = py_synth.Synthesizer(sample_rate=sample_rate)

    kick_sound = create_kick()

    print(f"Kick sound duration: {kick_sound.duration} seconds")
    print(f"Sample rate: {sample_rate.name}")
    print(f"Expected number of samples: {int(sample_rate.value * kick_sound.duration)}")

    synth.play_sound(kick_sound)
    synth.save_sound(kick_sound, "kick", "wav")
