# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:39:49 2021

@author: wantysal
"""

from mosqito.sound_level_meter.spectrum import spectrum

# Optional package import
try:
    import pytest
except ImportError:
    raise RuntimeError(
        "In order to perform the tests you need the 'pytest' package."
    )


# Local application imports
from mosqito.utils import load
from mosqito.sq_metrics import (
    tone_to_noise_ecma,
)


@pytest.mark.tnr  # to skip or run PR test
def test_tnr_ecma():
    """Test function for the prominence ratio calculation of an audio signal

    Validation function for the Audio_signal class "tone_to_noise_ecma" method with signal array
    as input. The input signals are generated using audacity.

    Parameters
    ----------
    None

    Outputs
    -------
    None
    """
    # Test signal as input for prominence ratio calculation
    # signals generated using audacity : white noise + tones at 200 and 2000 Hz
    # the first one is stationary, the second is time-varying
    signal = []

    signal.append(
        {
            "is_stationary": True,
            "tones freq": [200, 2000],
            "data_file": "tests/input/white_noise_442_1768_Hz_stationary.wav",
        }
    )

    signal.append(
        {
            "is_stationary": False,
            "data_file": "tests/input/white_noise_442_1768_Hz_varying.wav",
        }
    )

    for i in range(len(signal)):
        # Load signal
        audio, fs = load(signal[i]["data_file"])
        # Compute tone-to-noise ratio
        tnr = tone_to_noise_ecma(
            signal[i]["is_stationary"], audio, fs, prominence=True, overlap=0.5)


@pytest.mark.tnr  # to skip or run TNR test
def test_tnr_ecma_spec():
    """Test function for the prominence ratio calculation of an audio signal

    Validation function for the Audio_signal class "tone_to_noise_ecma" method with signal array
    as input. The input signals are generated using audacity.

    Parameters
    ----------
    None

    Outputs
    -------
    None
    """
    # Test signal as input for prominence ratio calculation
    # signals generated using audacity : white noise + tones at 200 and 2000 Hz
    # the first one is stationary, the second is time-varying
    signal = []

    signal.append(
        {
            "is_stationary": True,
            "data_file": "tests/input/white_noise_442_1768_Hz_stationary.wav",
        }
    )

    signal.append(
        {
            "is_stationary": False,
            "data_file": "tests/input/white_noise_442_1768_Hz_varying.wav",
        }
    )

    for i in range(len(signal)):
        # Load signal
        audio, fs = load(signal[i]["data_file"])
        # convert to frequency domain
        spec, freqs = spectrum(audio, fs, window='hanning', db=True)

        # Compute tone-to-noise ratio
        tnr = tone_to_noise_ecma(
            signal[i]["is_stationary"], spec, freqs=freqs, prominence=True
        )


if __name__ == "__main__":
    test_tnr_ecma()
