from scipy.fft import fft, ifft, fftfreq, fftshift
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


# number of signal points
N = 1024
# sampling freq
fs = 320000000  # 320 MHz
Ts = 1.0 / fs
x = np.linspace(0.0, N*Ts, N, endpoint=False)

# generate const signal
const = 1.0
real = const * np.ones(N)
imaj = const * np.ones(N)
y = real + imaj*1j
y[N//2] = 512 + 512j


yf = fft(y)
yplot = fftshift(yf)
print(yf)

xf = fftfreq(N, Ts)
xf = fftshift(xf)

#plt.plot(xf, 20 * np.log10(np.abs(yplot)))
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()

