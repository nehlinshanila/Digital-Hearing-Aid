import pyaudio
import wave
import scipy.io.wavfile as wavfile

# Set the parameters for the audio stream
chunk_size = 1024
sample_rate = 44100

wav_data = wavfile.read("test.wav")[1]

# Open the WAV file in read mode
# with wave.open('test.wav', 'rb') as wav_file:
    # Create a PyAudio object
p = pyaudio.PyAudio()

    # Open an audio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)

for i in range(0, len(wav_data), chunk_size):
    stream.write(wav_data[i:i+chunk_size].tobytes())


    # Stop the audio stream and terminate the PyAudio object
stream.stop_stream()
stream.close()
p.terminate()
