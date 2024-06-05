import numpy as np
from scipy.fft import fft, fftfreq
import scipy.io.wavfile as wavfile

# Define parameters
RATE = 44100
CHANNELS = 1
CHUNK_SIZE = 1024
BUFFER_SIZE = 10  # Number of chunks to buffer

# Calculate the length of the audio signal
lengthSignal = len(signalData)

# Apply Fourier Transform to the audio signal
fftSignal = fft(signalData)

# Get the frequencies of the audio signal
frequencies = fftfreq(lengthSignal, 1/samplingFrequency)

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

fig, ax = plt.subplots()
freq_axis = np.fft.fftfreq(CHUNK, d=1/RATE)
line, = ax.plot(freq_axis[:CHUNK//2], np.zeros(CHUNK//2))
ax.set_ylim(0, 200)


# !returns the data extracted from the audio input
def callback(in_data, frame_count, time_info, status):
    
    
    # *this is the input data or audio stream
    # print(in_data)
    data = np.frombuffer(in_data, dtype=np.int16) # Convert the input data to a NumPy array
    # print(data)
    
    # *filtered data
        # Wiener Filter: This filter can be used to estimate 
        # the original clean signal from the noisy signal by 
        # estimating the power spectral densities of the 
        # original signal and noise.
    # data = wiener(data)
    
    # *the root mean square of the audio signal
    # amp_data = np.frombuffer(amp_data, dtype=np.int16)
    amplitude = np.sqrt(np.mean(np.square(data)))
    # amplitude = 20 * math.log10(amplitude)
    threshhold = 100
    if(amplitude > threshhold):
        print("loud noise")
    # data2 = np.frombuffer(data, dtype=np.float32) # Convert the input data to a NumPy array
    # print(data2)
    fft_data = np.fft.fft(data) # Calculate the FFT of the data
    # print(fft_data)
    psd = np.abs(fft_data) ** 2 # Calculate the power spectral density (PSD) of the data
    # print(psd)
    psd = 10 * np.log10(psd) # Convert to dB
    psd = np.maximum(psd, -100)
    freq_bins = np.fft.fftfreq(len(psd)) * RATE # Calculate the frequency bins for the PSD
    # print(freq_bins)
    
    # *Find the peak frequency in the PSD
    peak_idx = np.argmax(psd)
    # print(peak_idx)
    peak_freq = freq_bins[peak_idx]
    # print(peak_freq)
    
    # *this is the max data of the amplitude got from the numpy array
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data)) #*updates the progress bar according to the sound density
    
    # data = in_data.read(CHUNK)
    # elapsed_time = len(in_data) / (RATE * CHANNELS * 2)
    # frecuency = (2 * np.pi * elapsed_time * RATE) / CHUNK
    
    
    # *this updates the frequency in real time
    _VARS['window']['Frequency'].update(f'{peak_freq:.2f} Hz') 
    
    # * this is where the amplitude updates regularly
    _VARS['window']['-Amplitude-'].update(f'{amplitude:.2f} dB')
    
    
    
    # * this is where the psd updates periodically
    # _VARS['window']['-PSD-'].update(f'{psd} W/Hz')
    
    plotting_fft_data = np.abs(np.fft.fft(data))
    
    line.set_ydata(plotting_fft_data[:CHUNK//2])
        
    
    
    # returning the data
    return (data, pyaudio.paContinue)


# this function controls the listen button of the UI
def listen():
    _VARS['window']['Stop'].Update(disabled=False)
    _VARS['window']['Listen'].Update(disabled=True)
    # this part enables the audio input
    # here we can talk using the microphone
    _VARS['stream'] = pAud.open(format=pyaudio.paInt16,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                output=True,
                                frames_per_buffer=CHUNK,
                                stream_callback=callback)

    _VARS['stream'].start_stream()
    
    
# *This is where the main loop happens
# *it's an infinite loop and it only stops when stop button is pressed
# *or the window is closed
while True:
    event, values = _VARS['window'].read(timeout=200)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        stop()    
        pAud.terminate()        
        break

# Get the frequency with the maximum amplitude
index = np.argmax(np.abs(fftSignal))
frequency = frequencies[index]
print("Frequency:", frequency)
