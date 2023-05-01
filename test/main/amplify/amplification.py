# THIS IS FOR INPUTTING SOUND AND AMPLIFYING IT AS OUTPUT

import pyaudio
import wave
import numpy as np

 # parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
AMPLIFICATION_FACTOR = 10.0


 # create instance
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT, 
                 channels=CHANNELS, 
                 rate=RATE, 
                 input=True, 
                 frames_per_buffer=CHUNK)



 # start recording
print("start recording=")

frames = []
seconds = 3
for i in range(0, int(RATE / CHUNK * seconds)):
     data = stream.read(CHUNK)
     frames.append(data)

print("recording stopped")

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


 # open the original WAV file for reading
with wave.open('output.wav', 'rb') as wavfile:
     # read the parameters of the original WAV file
     nchannels, sampwidth, framerate, nframes, comptype, compname = wavfile.getparams()
     # read the audio data from the original WAV file into a numpy array
     audio_data = np.frombuffer(wavfile.readframes(nframes), dtype=np.int16)
     # apply the amplification factor to the audio data
     amplified_data = (audio_data * AMPLIFICATION_FACTOR).astype(np.int16)

 # open a new WAV file for writing the amplified audio data
with wave.open('amplified_output.wav', 'wb') as new_wavfile:
     # set the parameters of the new WAV file to match the original
     new_wavfile.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
     # write the amplified audio data to the new WAV file
     new_wavfile.writeframes(amplified_data.tobytes())