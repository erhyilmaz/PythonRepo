# -------------------------------------------------------------------------------------------------------------------
# scipy.signal.iirfilter (N, Wn, rp=None, rs=None, btype='band', analog=False, ftype='butter', output='ba', fs=None)
# IIR digital and analog filter design given order and critical points.
# Design an Nth-order digital or analog filter and return the filter coefficients.
# -------------------------------------------------------------------------------------------------------------------
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Example 1
# Generate a 17th-order Chebyshev II analog bandpass filter from 50 Hz to 200 Hz
# and plot the frequency response:
b, a = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*200], rs=60, btype='band', analog=True, ftype='cheby2')
w, h = signal.freqs(b, a, 1000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()


# Example 2
# Create a digital filter with the same properties, in a system with sampling rate of 2000 Hz,
# and plot the frequency response. (Second-order sections implementation is required to ensure
# stability of a filter of this order):
sos = signal.iirfilter(17, [50, 200], rs=60, btype='band', analog=False, ftype='cheby2', fs=2000, output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=2000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()



