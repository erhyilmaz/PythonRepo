from scipy.fft import fft, ifft, fftfreq, fftshift
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as signal


# number of signal points
N = 1024
# sampling freq
fs = 320000000  # 320 MHz
Ts = 1.0 / fs

f = [5000000, 10000000, 15000000, 20000000, 25000000]
print(f)
# Time period
t = np.arange(0, N*Ts, Ts)

# Create a sine wave with multiple frequencies(1 Hz, 2 Hz and 4 Hz)
# xt = 7*np.cos(2 * np.pi * f[0] * t)
xt = 9*np.cos(2 * np.pi * f[0] * t) + 7*np.cos(2 * np.pi * f[1] * t) \
     + 5*np.cos(2 * np.pi * f[2] * t) + 3*np.cos(2 * np.pi * f[3] * t) + 1*np.cos(2 * np.pi * f[4] * t)
max_xt = max(xt)
xt = xt / (max_xt+1)

xt_re = xt.real  # real
xt_im = xt.imag  # imaginary

file_name = "./fft_input.txt"
with open(file_name, "w") as f:
    f.write('uint16_t real_arr_fix[1024] = { \n')

    # Convert to Q12.11 ADC output (-1, +1 range) Two's complement format
    for i in range(len(xt)):
        if xt_re[i] < 0:
            x_re_fix = hex(2 ** 16 - round(-xt_re[i] * 2 ** 11))
        else:
            x_re_fix = hex(round(xt_re[i] * 2 ** 11))

        if xt_im[i] < 0:
            x_im_fix = hex(2 ** 16 - round(-xt_im[i] * 2 ** 11))
        else:
            x_im_fix = hex(round(xt_im[i] * 2 ** 11))

        # print(f"{i} - {xt_re[i]} : {x_re_fix} : {x_im_fix} ")
        # f.write(x_re_fix +  x_im_fix + ', \n')
        if i == (len(xt)-1):
            f.write(x_re_fix + '};')
        else:
            f.write(x_re_fix + ',\n')

    if 0:
        # Plot the original cosine wave in time domain
        plt.plot(t, xt)
        plt.title("Cosine wave: cos(2*pi*f*t)")
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    # Do a Fourier transform on the signal
    Xf = fft(xt)
    f = fftfreq(N, Ts)

    # Plot the original sine wave using inverse Fourier transform
    # plt.plot(f, abs(Xf))
    # plt.plot(f, 10 * np.log10(abs(Xf)**2 / (fs*N)))
    plt.plot(f, 20 * np.log10(abs(Xf)/N))
    plt.title("Sine wave plotted using FFT")
    plt.xlabel('Freq')
    plt.ylabel('Amplitude')
    plt.ylim([-100, 0])
    plt.grid(True)
    plt.show()

    if 0:
        # Do an inverse Fourier transform on the signal
        xt_recover = ifft(Xf)

        # Plot the original sine wave using inverse Fourier transform
        plt.plot(t, xt_recover)
        plt.title("Sine wave plotted using inverse Fourier transform")
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

