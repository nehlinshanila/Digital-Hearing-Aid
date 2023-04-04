import pyaudio
import wave
import numpy as np

chunk = 1024  # samples per frame
channels = 2  # stereo
sample_rate = 44100  # samples per second
record_seconds = 10  # duration of recording
filename = "recording.wav"
threshold = 0.4

p = pyaudio.PyAudio()

# open audio stream
stream = p.open(format=pyaudio.paInt16, 
                channels=channels, 
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk)

# start recording
frames = []
for i in range(0, int(sample_rate / chunk * record_seconds)):
    data = stream.read(chunk)
    
    samples = np.frombuffer(data, dtype=np.int16)
    rms =np.abs(np.sqrt(np.mean(np.square(samples/32767)))) 
    print(rms)
    if rms < threshold:  
        frames.append(data)

# stop recording
stream.stop_stream()
stream.close()
p.terminate()

# write audio data to file
wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(sample_rate)
wf.writeframes(b"".join(frames))
wf.close()
