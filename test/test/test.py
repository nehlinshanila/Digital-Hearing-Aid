import numpy as np
from scipy.fft import fft, fftfreq
import scipy.io.wavfile as wavfile

# Load the audio file
samplingFrequency, signalData = wavfile.read('sample_audio.wav')

# Calculate the length of the audio signal
lengthSignal = len(signalData)

# Apply Fourier Transform to the audio signal
fftSignal = fft(signalData)

# Get the frequencies of the audio signal
frequencies = fftfreq(lengthSignal, 1/samplingFrequency)

# Plot the frequency spectrum of the audio signal
import matplotlib.pyplot as plt
plt.plot(frequencies, np.abs(fftSignal))
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()

# Get the frequency with the maximum amplitude
index = np.argmax(np.abs(fftSignal))
frequency = frequencies[index]
print("Frequency:", frequency)
