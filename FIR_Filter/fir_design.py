# import required library
import numpy as np
import scipy.signal.windows
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import firwin, remez, kaiser_atten, kaiser_beta, kaiserord, freqz, windows


def mfreqz(b, a, Fs):
    # Compute frequency response of the filter
    # using signal.freqz function
    wz, hz = signal.freqz(b, a)

    # Calculate Magnitude from hz in dB
    Mag = 20 * np.log10(abs(hz))

    # Calculate phase angle in degree from hz
    Phase = np.unwrap(np.arctan2(np.imag(hz), np.real(hz))) * (180 / np.pi)

    # Calculate frequency in Hz from wz
    Freq = wz * Fs / (2 * np.pi)

    # Plot filter magnitude and phase responses using subplot.
    fig = plt.figure(figsize=(10, 6))

    # Plot Magnitude response
    sub1 = plt.subplot(2, 1, 1)
    sub1.plot(Freq, Mag, 'r', linewidth=2)
    sub1.axis([1, Fs / 2, -100, 5])
    sub1.set_title('Magnitude Response', fontsize=20)
    sub1.set_xlabel('Frequency [Hz]', fontsize=20)
    sub1.set_ylabel('Magnitude [dB]', fontsize=20)
    sub1.grid()

    # Plot phase angle
    sub2 = plt.subplot(2, 1, 2)
    sub2.plot(Freq, Phase, 'g', linewidth=2)
    sub2.set_ylabel('Phase (degree)', fontsize=20)
    sub2.set_xlabel(r'Frequency (Hz)', fontsize=20)
    sub2.set_title(r'Phase response', fontsize=20)
    sub2.grid()

    plt.subplots_adjust(hspace=0.5)
    fig.tight_layout()
    plt.show()


# Define impz(b,a) to calculate impulse response and step response of a system
# input: b= an array containing numerator coefficients,
#        a= an array containing denominator coefficients
def impz(b, a):
    # Define the impulse sequence of length 100
    impulse = np.repeat(0., 100)
    impulse[0] = 1.
    x = np.arange(0, 100)

    # Compute the impulse response
    response = signal.lfilter(b, a, impulse)

    # Plot filter impulse and step response:
    fig = plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.stem(x, response, 'm')
    plt.ylabel('Amplitude', fontsize=15)
    plt.xlabel(r'n (samples)', fontsize=15)
    plt.title(r'Impulse response', fontsize=15)

    # Compute step response of the system
    step = np.cumsum(response)

    plt.subplot(2, 1, 2)
    plt.stem(x, step, 'g')
    plt.ylabel('Amplitude', fontsize=15)
    plt.xlabel(r'n (samples)', fontsize=15)
    plt.title(r'Step response', fontsize=15)

    plt.subplots_adjust(hspace=0.5)
    fig.tight_layout()
    plt.show()


# --------------------------------------------------------------------
# Low-pass FIR filter Design:
# --------------------------------------------------------------------
# f_width    Width of the transition from pass to stop freq in Hz
# cutoff_hz  Cut-off frequency in Hz
# F_samp     Sampling frequency in Hz
# A_stop     Stop band attenuation in dB
# window     window-type is kaiser
def lowpass_firwin(f_width, cutoff_hz, A_stop, F_samp):

    nyq_freq = F_samp / 2
    fp = cutoff_hz - f_width / 2  # Pass band frequency in Hz
    fs = cutoff_hz + f_width / 2  # Stop band frequency in Hz
    # Compute pass band and stop band edge frequencies
    wp = fp / nyq_freq  # Normalized pass-band edge frequencies
    ws = fs / nyq_freq  # Normalized stop-band edge frequencies

    # Compute the order and Kaiser parameter for the FIR filter.
    ntaps, beta = kaiserord(A_stop, f_width / nyq_freq)
    print(f"N_taps: {ntaps}, beta: {beta}")

    # Use 'firwin()' with a Kaiser window to create a low-pass FIR filter.
    taps = firwin(ntaps, cutoff=cutoff_hz/nyq_freq, window=('kaiser', beta))

    # taps = firwin(131, cutoff=cutoff_hz/nyq_freq, window=('chebwin', 60))
    # taps = firwin(131, cutoff=cutoff_hz/nyq_freq, window="hamming")
    # taps = firwin(131, cutoff=cutoff_hz/nyq_freq, window='flattop')
    # taps = firwin(131, cutoff=cutoff_hz/nyq_freq, window=('gaussian', 5))

    print(f"taps ({len(taps)}) : {taps}")

    return taps


if __name__ == "__main__":

    # Sample rate and desired cutoff frequencies (in Hz).
    MHz = 1000000        # MHz alias
    Fsamp = 320 * MHz    # Sampling frequency in Hz
    f_cutoff = 40 * MHz  # Pass band frequency in Hz
    f_width = 10 * MHz    # width of the transition from pass to stop frequency in Hz
    A_stop = 50          # Stop band attenuation in dB

    fir_taps_kaiser = lowpass_firwin(f_width, f_cutoff, A_stop, Fsamp)

    # Call mfreqz() to plot the magnitude and phase response
    mfreqz(fir_taps_kaiser, 1, Fsamp)

    # Call impz() function to plot impulse and step response of the filter
    # impz(fir_taps_kaiser, 1)
