import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


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


# Define impz(b,a) to calculate impulse response
# and step response of a system
# input: b= an array containing numerator coefficients,
# a= an array containing denominator coefficients
def impz(b, a):
    # Define the impulse sequence of length 60
    impulse = np.repeat(0., 60)
    impulse[0] = 1.
    x = np.arange(0, 60)

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


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Given specification
MHz = 1000000    # MHz alias
Fsamp = 320*MHz  # Sampling frequency in Hz
fp = 37*MHz      # Pass band frequency in Hz
fs = 47*MHz      # Stop band frequency in Hz
# Compute pass band and stop band edge frequencies
wp = fp/(Fsamp/2)  # Normalized pass-band edge frequencies w.
ws = fs/(Fsamp/2)  # Normalized stop-band edge frequencies
# Gain values
gpass = 1       # Pass band ripple in dB
gstop = 57      # Stop band attenuation in dB

# Complete IIR digital and analog filter design:
# scipy.signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba', fs=None)
# ftypestr, optional (The type of IIR filter to design):
#        Butterworth   : ‘butter’
#        Chebyshev I   : ‘cheby1’
#        Chebyshev II  : ‘cheby2’
#        Cauer/elliptic: ‘ellip’

b, a = signal.iirdesign(wp, ws, gpass, gstop, ftype='ellip', output='ba')

# Print numerator and denominator coefficients of the filter
print(f'Numerator (b) Coefficients {len(b)} : {b}')
print(f'Denominator (a) Coefficients {len(a)} : {a}')

# Call mfreqz() to plot the magnitude and phase response
mfreqz(b, a, Fsamp)

# Call impz() function to plot impulse and step response of the filter
impz(b, a)
