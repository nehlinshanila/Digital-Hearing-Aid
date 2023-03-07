import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.animation as animation
import pyaudio

# Parameters
CHUNK = 1024 # Number of samples per chunk
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 # Sampling rate (Hz)
WINDOW = mlab.window_hanning # Window function
NFFT = CHUNK # Number of FFT points
DETREND = mlab.detrend_none # Detrend function
FS = RATE / NFFT # Frequency resolution (Hz)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(0, FS/2)
ax.set_ylim(-100, 100)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Power (dB/Hz)')
line, = ax.plot([], [])

# Update function
def update(data):
    # Compute PSD
    psd, freqs = mlab.psd(data, Fs=RATE, NFFT=NFFT, window=WINDOW, detrend=DETREND)
    psd = 10 * np.log10(psd) # Convert to dB
    psd = np.maximum(psd, -100) # Clip to prevent numerical problems
    
    # Update plot
    line.set_data(freqs, psd)
    return line,

# Animation function
def animate(i):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    return update(data)

# Start animation
ani = animation.FuncAnimation(fig, animate, blit=True, interval=0)

# Show plot
plt.show()

# Stop audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
