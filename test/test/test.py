import PySimpleGUI as sg #for the UI design
import pyaudio #for the input of the audio
import numpy as np #for numaric and mathematical calculationssuch as fourier
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.animation as animation
import math
from scipy.signal import lfilter, wiener

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
        #   [sg.Text('PSD:', font=AppFont),
        #    sg.Text(unit_psd0, key='-PSD-', font=AppFont)]
          [sg.Button('Listen', key='Listen', font=AppFont),
           sg.Button('Stop', key='Stop', font=AppFont, disabled=True),
           sg.Button('Exit', key='Exit', font=AppFont)],
          [sg.Button('Frequency-Plot', key='-FreqPlot-', font=AppFont)]]

# finalizing the window UI
_VARS['window'] = sg.Window('Microphone Level', layout, finalize=True)


# canvas = _VARS['window']['-CANVAS-'].TKCanvas
# line = canvas.create_line((0, 150, 400, 150), fill='red', width=2)

# *initiating constants for the audio stream data
CHUNK = 128  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen
CHANNELS = 1
freq_bins = None
psd = None

# for the PSD data
FORMAT = pyaudio.paInt16
WINDOW = mlab.window_hanning # Window function
NFFT = CHUNK # Number of FFT points
DETREND = mlab.detrend_none # Detrend function
FS = RATE / NFFT # Frequency resolution (Hz)


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
        _VARS['window']['Frequency'].Update(unit_freq0)
        _VARS['window']['-Amplitude-'].Update(unit_amp0)
        # _VARS['window']['-PSD-'].Update(unit_psd0)


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
    if event == 'Listen':
        listen()
    if event == 'Stop':
        stop()
    if event == '-FreqPlot-':
        state = _VARS['window'].Element('Listen').Disabled
        while state == True:
            plt.draw()
            plt.pause(0.001)

                
        #     print("enabled")
        # else:
        #     print("disabled")
        
        
        
    # canvas.delete(line)
    # line = canvas.create_line([(freq_bins[i], 300 -10 * np.log10(psd[i]))
    #                            for i in range(len(psd) //2)], 
    #                           fill='red', width=2)

# clsoe the window UI anyway after the loop
_VARS['window'].close()