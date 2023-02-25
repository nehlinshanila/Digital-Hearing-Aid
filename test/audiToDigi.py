import wave
import numpy as np
import matplotlib.pyplot as plt

# # Open the audio file
# with wave.open("audio.wav", "rb") as audio_file:
#     # Read the audio file frames
#     frames = audio_file.readframes(audio_file.getnframes())
    
#     # Convert the frames to bytes
#     bytes_data = list(frames)
    
#     # Convert the bytes to integers
#     ints_data = [int.from_bytes(bytes_data[i:i+2], byteorder='little', signed=True) for i in range(0, len(bytes_data), 2)]
    
#     # Reshape the integer array into a 2D numpy array
#     n_channels = audio_file.getnchannels()
#     n_frames = len(ints_data) // n_channels
#     audio_signal = np.reshape(ints_data, (n_frames, n_channels))
    
#     # Normalize the audio signal
#     audio_signal = audio_signal.astype(np.float32) / 32768.0
    
digital_signal = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
plt.step(range(len(digital_signal)), digital_signal, where='post')
plt.ylim([-0.1, 1.1])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Digital Signal')
plt.show()
