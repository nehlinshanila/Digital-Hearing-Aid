import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wavio as wv



wav = wv.read('test1.wav')
wav_data = wav.data.astype(float)

# Open the WAV file in read mode
# with wave.open('test.wav', 'rb') as wav_file:
    # Create a PyAudio object
p = pyaudio.PyAudio()

print("Playing audio")
    # Open an audio stream
stream = p.open(format=p.get_format_from_width(wav.sampwidth), 
            channels=wav.sampwidth // 2 , 
            rate=wav.rate, 
            output=True)

# Initialize PyAudio

# Set the parameters for the audio stream
sample_rate = 44100
duration = 2
chunk_size = 1024



# Open an audio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

# Read audio data from the stream
frames = []
for i in range(int(sample_rate / chunk_size * duration)):
    data = stream.read(chunk_size)
    frames.append(data)

# Convert the audio data to a numpy array
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Compute the FFT of the audio data
fft_data = np.abs(np.fft.fft(audio_data))

# Convert the FFT data to a digital signal
threshold = np.max(fft_data) * 0.8
digital_data = (fft_data > threshold).astype(int)

# Plot the digital signal
plt.step(range(len(digital_data)), digital_data, where='post')
plt.ylim([-0.1, 1.1])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Digital Signal')
plt.show()
