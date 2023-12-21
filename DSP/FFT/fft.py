import numpy as np
import matplotlib.pyplot as plt

# Generate a sample time series dataset
# You can replace this with your own time series data
# Ensure that the data is in a NumPy array or a list
time = np.arange(0, 10, 0.01)  # Time values from 0 to 10 with a step of 0.01
signal = 2 * np.sin(2 * np.pi * 1 * time) + 1 * np.sin(2 * np.pi * 2 * time)

# Plot the original time series
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title('Original Time Series')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Perform the Fourier Transform
fourier_transform = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 0.01)  # Frequency values (assuming a sampling interval of 0.01)

# Plot the magnitude of the Fourier Transform
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fourier_transform))
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 5)  # Limit the x-axis to show frequencies up to 5 Hz

plt.tight_layout()
plt.show()