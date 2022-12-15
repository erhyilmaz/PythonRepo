import numpy as np
from scipy.fft import fft, ifft, fftfreq, fftshift, rfft, irfft
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal.windows import blackman

if 0:
    # ==============================================
    # FFT and IFFT functions
    # ==============================================
    x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
    y = fft(x)
    print(y)
    yinv = ifft(y)
    print(yinv)


    # =======================================================
    # FFT function
    # The example plots the FFT of the sum of two sines.
    # =======================================================
    # Number of sample points
    N = 1024
    # sample spacing, period
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N, endpoint=False)
    print(len(x))
    print(type(x))
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)  # signal at 50Hz and 80Hz, sampled @ 800Hz
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]

    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.show()

    # ===============================================================
    # FFT function + Windowing
    # The example below uses a Blackman window from 'scipy.signal'
    # and shows the effect of windowing (the zero component of the FFT
    # has been truncated for illustrative purposes).
    # ===============================================================

    # Number of sample points
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N, endpoint=False)
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    yf = fft(y)

    w = blackman(N)
    ywf = fft(y*w)
    xf = fftfreq(N, T)[:N//2]

    plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
    plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), '-r')
    plt.legend(['FFT', 'FFT w. window'])
    plt.grid()
    plt.show()


# ===============================================================
# Complex FFT function
# The example below plots the FFT of two complex exponentials;
# note the asymmetric spectrum.
# ===============================================================
# number of signal points
N = 400
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.exp(50.0 * 1.j * 2.0*np.pi*x) + 0.5*np.exp(-80.0 * 1.j * 2.0*np.pi*x)  # complex exponentials
yf = fft(y)
xf = fftfreq(N, T)

xf = fftshift(xf)
yplot = fftshift(yf)

plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()


# =========================================================================================================
# Note: The function rfft calculates the FFT of a real sequence and
# outputs the complex FFT coefficients for only half of the frequency range.
# The remaining negative frequency components are implied
# by the Hermitian symmetry of the FFT for a real input (y[n] = conj(y[-n])).
# In case of N being even: ; in case of N being odd . The terms shown explicitly as
# are restricted to be purely real since, by the hermitian property, they are their own complex conjugate.
# The corresponding function irfft calculates the IFFT of the FFT coefficients with this special ordering.
# =========================================================================================================


