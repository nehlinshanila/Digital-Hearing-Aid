import struct
import PySimpleGUI as sg #for the UI design
import pyaudio #for the input of the audio
import numpy as np #for numaric and mathematical calculationssuch as fourier
import math
from scipy.signal import lfilter, wiener
import wave as wv
from scipy.fft import fft, fftfreq
import time
"""PyAudio PySimpleGUI Non Blocking Stream for Microphone"""

# *VARS contants that will control the window's UI and the UI of the Audio stream
_VARS = {'window': False, #this will hold the UI window as a variable/constant
         'stream': False, #this will hold the audio stream as a variable/constant
        #  'canvas': False
         }

# pysimpleGUI initiation
# here we initiate the overall UI and then control afterwards

AppFont = 'Any 16' #this is the font variable

# the theme of the UI
sg.theme('DarkTeal2')


unit_amp0 = '0 dB'
unit_freq0 = '0 Hz'
unit_psd0 = '0 W/Hz'

# *this here customizes the layout
layout = [[sg.ProgressBar(4000, orientation='h',
                          size=(20, 20), key='-PROG-')],
          [sg.Text('Frequency:', font=AppFont),
           sg.Text(unit_freq0, key='Frequency',font=AppFont)],
          [sg.Text('Amplitude:', font=AppFont),
           sg.Text(unit_amp0, key='-Amplitude-', font=AppFont)],
          [sg.Text('Elapsed Time:', font=AppFont),
           sg.Text('0 s' , key='-elapsedTime-', font=AppFont)],
          [sg.Button('Listen', key='Listen', font=AppFont),
           sg.Button('Stop', key='Stop', font=AppFont, disabled=True),
           sg.Button('Exit', key='Exit', font=AppFont)]]

# finalizing the window UI
_VARS['window'] = sg.Window('Microphone Level', layout, finalize=True)


# canvas = _VARS['window']['-CANVAS-'].TKCanvas
# line = canvas.create_line((0, 150, 400, 150), fill='red', width=2)

# *initiating constants for the audio stream data
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 48000  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen
CHANNELS = 1
freq_bins = None
psd = None
start = 0.00
end = 0.00
elapsed_time = 0.00

# for the PSD data
FORMAT = pyaudio.paInt16
# WINDOW = mlab.window_hanning # Window function
# NFFT = CHUNK # Number of FFT points
# DETREND = mlab.detrend_none # Detrend function
# FS = RATE / NFFT # Frequency resolution (Hz)

TIME_OF_RECORD = 5
WAVE_OUTPUT_FILENAME = 'testOutput.wav'

frames = []

# PyAudio initiation
pAud = pyaudio.PyAudio()



# FUNCTIONS:

# *this controls the stop button of the UI
#  !All the UI are reset here
def stop():
    
    if _VARS['stream']:
        _VARS['stream'].stop_stream()
        _VARS['stream'].close()
        _VARS['window']['-PROG-'].update(0)
        _VARS['window']['Stop'].Update(disabled=True)
        _VARS['window']['Listen'].Update(disabled=False)
        # _VARS['window']['Frequency'].Update(unit_freq0)
        # _VARS['window']['-Amplitude-'].Update(unit_amp0)
        end = time.time()
        elapsed_time = end - start
        _VARS['window']['-elapsedTime-'].Update(str(f'{elapsed_time:.2f} seconds'))

        #!this here works for the saving of the wave file
        # wf = wv.open('WAVE_OUTPUT_FILENAME', 'wb')
        # wf.setnchannels(CHANNELS)
        # wf.setsampwidth(pAud.get_sample_size(FORMAT))
        # wf.setframerate(RATE)
        # wf.writeframes(b''.join(frames))
        # wf.close()

# !returns the data extracted from the audio input
def callback(in_data, frame_count, time_info, status):
    #!appending input sound data to the audio
    # frames.append(in_data)

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
    # amplitude = np.sqrt(np.mean(np.square(data)))
    # amplitude = 20 * math.log10(amplitude)
    
    # data2 = np.frombuffer(data, dtype=np.float32) # Convert the input data to a NumPy array
    # print(data2)
    # fft_data = np.fft.fft(data) # Calculate the FFT of the data
    # fft_data = fft(data)
    # num_sample = len(data)
    # freq_res = num_sample / float(RATE)
    # fft_magnitude = np.abs(fft_data)
    # frequencies = np.linspace(0, RATE/2, num_sample//2 + 1)
    # freq = fft_magnitude[:num_sample//2 + 1] / frequencies
    # frequencies = num_sample / freq_res
    # print(fft_data)
    # psd = np.abs(fft_data) ** 2 # Calculate the power spectral density (PSD) of the data
    # print(psd)
    # psd = 10 * np.log10(psd) # Convert to dB
    # psd = np.maximum(psd, -100) #limiting the power spectral density

    # freq_bins = np.fft.fftfreq(len(psd)) * RATE # Calculate the frequency bins for the PSD
    # print(freq_bins)
    
    # *Find the peak frequency in the PSD
    # peak_idx = np.argmax(psd)
    # print(peak_idx)
    # peak_freq = freq_bins[peak_idx]
    # print(peak_freq)
    
    # *this is the max data of the amplitude got from the numpy array
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data)) #*updates the progress bar according to the sound density
    
    # data = in_data.read(CHUNK)
    # elapsed_time = len(in_data) / (RATE * CHANNELS * 2)
    # frecuency = (2 * np.pi * elapsed_time * RATE) / CHUNK
    
    
    # *this updates the frequency in real time
    # if peak_freq > 200.00:
    # _VARS['window']['Frequency'].update(f'{frequencies:.2f} Hz')
    
    freqs = np.fft.fftfreq(len(data), d=1/RATE)
    fft = np.fft.fft(data)
    index = np.argmax(np.abs(fft))
    freq = freqs[index]
    # if freq > 200.00:
    _VARS['window']['Frequency'].update(f'{freq:.2f} Hz')
    # print(f'{freq:.2f} Hz')
    # else:
    # _VARS['window']['Frequency'].update('0 Hz')
    # print('0 Hz')
        
    
    
    # * this is where the amplitude updates regularly
    # if amplitude > 10.00:
    # _VARS['window']['-Amplitude-'].update(f'{amplitude:.2f} dB')
    rms = np.sqrt(np.mean(np.square(data)))
    _VARS['window']['-Amplitude-'].update(f'{rms:.2f} dB')
    print(f'{rms:.2f} dB')
    # if the amplitude of the sound is over 20 it will be considered as loud sound
    
    # _VARS['window']['-Amplitude-'].update( '10 dB')
    
    
    
    # * this is where the psd updates periodically
    # _VARS['window']['-PSD-'].update(f'{psd} W/Hz')
    amplified_data = [min(int(sample * 2), 32767) for sample in struct.unpack(f"<{frame_count}h", in_data)]

    # returning the data
    return (struct.pack(f"<{frame_count}h", *amplified_data), pyaudio.paContinue)


# this function controls the listen button of the UI
def listen():
    start = time.time()
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

    #!reading the whole audio stream data and saving it using loop
    # for i in range(0, int(RATE / CHUNK * TIME_OF_RECORD)):
    #     data = _VARS['stream'].read(CHUNK)
    
# PSD starts


# PSD ends
    
    
# *This is where the main loop happens
# *it's an infinite loop and it only stops when stop button is pressed
# *or the window is closed
while True:
    event, values = _VARS['window'].read(timeout=200)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        stop()    
        pAud.terminate()        
        break
    if event == 'Listen':
        start = time.time()
        listen()
    if event == 'Stop':
        stop()
        
    if event == '-deAmp-':
        limiter_gain -= 0.1
    if event == '-Amp-':
        limiter_gain +=0.1
        
    if event == '-DelimiterTreshold-':
        limiter_threshold_value -= 0.1
    if event == '-DelimiterTreshold-':
        limiter_threshold_value +=0.1
        
# clsoe the window UI anyway after the loop
_VARS['window'].close()