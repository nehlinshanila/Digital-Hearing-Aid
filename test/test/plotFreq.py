import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the pyaudio stream
chunk_size = 1024
sample_rate = 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                input=True, output=True, frames_per_buffer=chunk_size)

# Initialize the plot
fig, ax = plt.subplots()
freq_axis = np.fft.fftfreq(chunk_size, d=1/sample_rate)
line, = ax.plot(freq_axis[:chunk_size//2], np.zeros(chunk_size//2))

# Define the animation function
def update(frame):
    # Read the audio data from the stream
    data = stream.read(chunk_size, exception_on_overflow=False)

    # Convert the audio data to a numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Calculate the Fourier transform of the audio data
    fft_data = np.abs(np.fft.fft(audio_data))

    # Update the plot
    line.set_ydata(fft_data[:chunk_size//2])
    
    # print(line)
    return line,

# Start the animation
ani = FuncAnimation(fig, update, blit=True)
plt.show()

# Close the pyaudio stream
stream.stop_stream()
stream.close()
p.terminate()
