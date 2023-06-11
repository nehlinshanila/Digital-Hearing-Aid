import pyaudio
import numpy as np

chunk_size = 1024  # number of audio samples per frame
sample_rate = 44100  # Hz
threshold = 0.4  # adjust as needed

# initialize PyAudio
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate,
                 input=True, frames_per_buffer=chunk_size)

# continuously read audio samples and check for loud noises
while True:
    # read audio chunk from stream
    data = stream.read(chunk_size)
    # convert to numpy array
    samples = np.frombuffer(data, dtype=np.float32)
    # calculate root-mean-square (RMS) amplitude of samples
    rms = np.sqrt(np.mean(samples**2))
    print(rms)
    # check if amplitude exceeds threshold
    if rms > threshold:
        print("Loud noise detected!")
