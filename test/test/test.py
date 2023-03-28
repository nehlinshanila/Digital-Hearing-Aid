import pyaudio
import numpy as np
import scipy.signal as signal
import time

# Define parameters
RATE = 44100
CHANNELS = 1
CHUNK_SIZE = 1024
BUFFER_SIZE = 10  # Number of chunks to buffer

# Create a low-pass filter
fc = 4000  # Cutoff frequency
b, a = signal.butter(4, fc / (RATE / 2), 'low')

# Define callback function to process audio stream
def audio_callback(in_data, frame_count, time_info, status):
    # Convert input audio to numpy array
    audio_data = np.frombuffer(in_data, dtype=np.int16)

    # Apply Wiener filter
    filtered_data = signal.wiener(audio_data)

    # Apply low-pass filter
    filtered_data = signal.filtfilt(b, a, filtered_data)

    # Convert filtered audio back to bytes-like object
    out_data = filtered_data.astype(np.int16).tobytes()

    return (out_data, pyaudio.paContinue)

# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK_SIZE,
                stream_callback=audio_callback)

# Start audio stream
stream.start_stream()

# Keep stream running for BUFFER_SIZE chunks
while stream.is_active():
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

# Stop audio stream
stream.stop_stream()
stream.close()
p.terminate()
