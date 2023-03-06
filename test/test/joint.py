# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import pyaudio
import wave
import scipy.io.wavfile as wavfile
import numpy as np
import soundfile as sf


# Sampling frequency
freq = 44100
chunk_size = 1024
sample_rate = 44100
# Recording duration
duration = 2

print("Recording...")

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()
print("Recording done")

# recording = recording.astype(np.int32)
# This will convert the NumPy array to an audio
# file with the given sampling frequency
# write("test.wav", freq, recording)
wv.write("test1.wav", recording, freq, sampwidth=2)




# wav_data = wavfile.read("test1.wav")[1]
# wav = wv.read('test1.wav')
# wav_data = wav.data.astype(float)

# # Open the WAV file in read mode
# # with wave.open('test.wav', 'rb') as wav_file:
#     # Create a PyAudio object
# p = pyaudio.PyAudio()

# print("Playing audio")
#     # Open an audio stream
# stream = p.open(format=p.get_format_from_width(wav.sampwidth), 
#             channels=wav.sampwidth // 2 , 
#             rate=wav.rate, 
#             output=True)

# for i in range(0, len(wav_data), wav.rate):
#     chunk = wav_data[i:i+wav.rate, :]
#     # stream.write(wav_data[i:i+chunk_size].tobytes())
#     stream.write(chunk.astype(wv.wavio.FLOAT32).tobytes())


#     # Stop the audio stream and terminate the PyAudio object
# stream.stop_stream()
# stream.close()
# p.terminate()

data , fs = sf.read("test1.wav", dtype='float32')
sd.play(data, fs)

status = sd.wait()