import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

# Initialize the pyaudio stream
chunk_size = 1024
sample_rate = 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                input=True, frames_per_buffer=chunk_size)

# Initialize the plot
fig, ax = plt.subplots()
freq_axis = np.fft.fftfreq(chunk_size, d=1/sample_rate)
line, = ax.plot(freq_axis[:chunk_size//2], np.zeros(chunk_size//2))
ax.set_ylim(0, 50000)

# Continuously plot the frequency spectrum
while True:
    # Read the audio data from the stream
    data = stream.read(chunk_size, exception_on_overflow=False)

    # Convert the audio data to a numpy array
    data = np.frombuffer(data, dtype=np.int16)

    # data = wiener(data)
    # Calculate the Fourier transform of the audio data
    fft_data = np.abs(np.fft.fft(data))

    # Update the plot
    line.set_ydata(fft_data[:chunk_size//2])
    plt.draw()
    plt.pause(0.001)

# Close the pyaudio stream
stream.stop_stream()
stream.close()
p.terminate()
