import pyaudio
import wave
import numpy as np

chunk = 1024  # samples per frame
channels = 2  # stereo
sample_rate = 44100  # samples per second
record_seconds = 5  # duration of recording
filename = "recording.wav"
threshold = 0.4

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    
    return (in_data, pyaudio.paContinue)

# open audio stream
stream = p.open(format=pyaudio.paInt16, channels=channels, rate=sample_rate,
                input=True, output=True, frames_per_buffer=chunk)

# start recording
frames = []
for i in range(0, int(sample_rate / chunk * record_seconds)):
    data = stream.read(chunk)
    samples = np.frombuffer(data, dtype=np.float32)
    # calculate root-mean-square (RMS) amplitude of samples
    rms = np.sqrt(np.mean(samples**2))
    # if rms < threshold:
    print(rms)
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
