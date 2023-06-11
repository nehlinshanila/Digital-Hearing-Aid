import numpy as np
from pydub import AudioSegment

# Load audio file
audio_file = AudioSegment.from_wav("test.wav")

# Extract raw audio data and convert to numpy array
raw_audio = audio_file.get_array_of_samples()
raw_audio = np.array(raw_audio)

# Define denoising parameters
frame_size = 1024
hop_size = 512
threshold = 30

# Split audio into frames and compute power spectrum
frames = np.array([raw_audio[i:i+frame_size] for i in range(0, len(raw_audio)-frame_size, hop_size)])
power_spec = np.abs(np.fft.rfft(frames))**2

# Compute noise floor and subtract from power spectrum
noise_floor = np.mean(power_spec[:, :threshold], axis=1)
power_spec_denoised = np.maximum(power_spec - noise_floor[:, np.newaxis], 0)

# Inverse FFT and overlap-add
frames_denoised = np.fft.irfft(np.sqrt(power_spec_denoised)) * frame_size
out_audio = np.zeros((len(raw_audio),))
for i in range(len(frames_denoised)):
    out_audio[i*hop_size:i*hop_size+frame_size] += frames_denoised[i]

# Convert output audio to PyDub AudioSegment and save to file
out_audio = np.int16(out_audio)
out_audio_file = AudioSegment(out_audio.tobytes(), frame_rate=audio_file.frame_rate, sample_width=2, channels=1)
out_audio_file.export("output_audio.wav", format="wav")
