import pyaudio
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt


# Set up the recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Create an instance of the PyAudio class
p = pyaudio.PyAudio()

# Open a new audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Record the audio data
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Close the audio stream
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()



# Read in the WAV file
rate, data = wavfile.read('output.wav')

# Plot the digital signal
plt.plot(data)
plt.show()

