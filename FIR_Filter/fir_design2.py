#!python
import numpy as np
from numpy import cos, sin, pi, absolute, arange
from numpy.random import randn
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

# ------------------------------------------------
# Create a signal for demonstration.
# ------------------------------------------------
# Sample rate and desired cutoff frequencies (in Hz).
MHz = 1000000            # MHz alias
sample_rate = 320 * MHz  # Sampling frequency in Hz
nsamples = 1024

t = arange(nsamples) / sample_rate
x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
        0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
        0.1*sin(2*pi*23.45*t+.8) + 0.08 * randn(len(t))

# ------------------------------------------------
# Create a FIR filter and apply it to x.
# ------------------------------------------------
f_cutoff = 40 * MHz  # Pass band frequency in Hz
f_width  = 10 * MHz  # width of the transition from pass to stop frequency in Hz
A_stop   = 60        # Stop band attenuation in dB

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0

# The desired width of the transition from pass to stop, relative to the Nyquist rate.
# We'll design the filter with a 5 Hz transition width.
width = f_width/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = A_stop

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_hz = f_cutoff

# Use firwin with a Kaiser window to create a lowpass FIR filter.
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

# Use lfilter to filter x with the FIR filter.
filtered_x = lfilter(taps, 1.0, x)

# ------------------------------------------------
# Plot the FIR filter coefficients.
# ------------------------------------------------

figure(1)
plot(taps, 'bo-', linewidth=2)
title('Filter Coefficients (%d taps)' % N)
grid(True)

# ------------------------------------------------
# Plot the magnitude response of the filter.
# ------------------------------------------------

figure(2)
clf()
w, h = freqz(taps, worN=2**13)
plot((w/pi)*nyq_rate, 20*np.log10(abs(h)), linewidth=2)
xlabel('Frequency (Hz)')
ylabel(r'$\|H(f)\|^2$')
title('Filter Frequency Response')
ylim(-100, 5)
grid(True)

# ------------------------------------------------
# Plot the original and filtered signals.
# ------------------------------------------------

# The phase delay of the filtered signal.
delay = 0.5 * (N-1) / sample_rate

figure(3)
# Plot the original signal.
plot(t, x)
# Plot the filtered signal, shifted to compensate for the phase delay.
plot(t-delay, filtered_x, 'r-')
# Plot just the "good" part of the filtered signal.  The first N-1 samples are "corrupted" by the initial conditions.
plot(t[N-1:]-delay, filtered_x[N-1:], 'g', linewidth=4)

xlabel('t')
grid(True)

show()

