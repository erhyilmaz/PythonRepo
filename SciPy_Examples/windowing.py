import numpy as np
from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

# ================================================================
# Windowing functions for Filtering and Spectral Estimation.
# ================================================================
window = signal.windows.kaiser(51, beta=14, sym=True)

fig = plt.figure(figsize=(10, 6))

sub1 = plt.subplot(2, 1, 1)
sub1.plot(window)
sub1.set_title(r"Kaiser window ($\beta$=14)")
sub1.set_ylabel("Amplitude")
sub1.set_xlabel("Sample")
sub1.grid()

# Frequency Response of the windowing filter
A = fft(window, 2048) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))  # normalized frequencies [-pi, +pi] or [-fs/2, fs/2]
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))

sub2 = plt.subplot(2, 1, 2)
sub2.plot(freq, response)
sub2.axis([-0.5, 0.5, -120, 0])
sub2.set_title(r"Frequency response of the Kaiser window ($\beta$=14)")
sub2.set_ylabel("Normalized magnitude [dB]")
sub2.set_xlabel("Normalized frequency [cycles per sample]")
sub2.grid()

plt.subplots_adjust(hspace=0.5)
fig.tight_layout()
plt.show()



