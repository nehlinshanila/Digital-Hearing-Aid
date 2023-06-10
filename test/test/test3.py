import pyaudio
import struct

chunk_size = 1024
scale_factor = 2

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                output=True,
                frames_per_buffer=chunk_size)

while True:
    # Read a chunk of audio data from the stream
    data = stream.read(chunk_size)
    
    # Unpack the binary data into a list of samples
    samples = struct.unpack(f"{chunk_size}h", data)
    
    # Scale the amplitude of each sample
    scaled_samples = [int(sample * scale_factor) for sample in samples]
    
    # Pack the scaled samples back into binary data
    scaled_data = struct.pack(f"{chunk_size}h", *scaled_samples)
    
    # Write the scaled data back to the stream
    stream.write(scaled_data)
