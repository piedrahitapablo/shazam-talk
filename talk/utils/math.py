import numpy as np


def wave(time, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * time)


def superposed_waves(time, params):
    return np.sum(np.array([wave(time, a, f) for a, f in params]), axis=0)


def sampling_times(t0, t1, sampling_freq):
    period = 1 / sampling_freq
    n_samples = ((t1 - t0) // period) + 1
    actual_t1 = t1 - ((t1 - t0) % period)

    return np.linspace(t0, actual_t1, int(n_samples))


def whittaker_shannon(time, samples, samples_times):
    period = samples_times[1] - samples_times[0]

    reconstructed = np.sum(
        np.array([samples * np.sinc((t - samples_times) / period) for t in time]),
        axis=1,
    )

    return reconstructed
