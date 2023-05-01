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


unit_amp0 = '1 dB'
unit_freq0 = '1 Hz'
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
CHUNK = 2048  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
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
        # _VARS['window']['Frequency'].Update(f'{last_freq:.2f} Hz')
        # _VARS['window']['-Amplitude-'].Update(f'{last_amp:.2f} dB')
        end = time.time()
        elapsed_time = end - start
        _VARS['window']['-elapsedTime-'].Update(str(f'{elapsed_time:.2f} seconds'))

# !returns the data extracted from the audio input
def callback(in_data, frame_count, time_info, status):
    

    # *this is the input data or audio stream
    
    data = np.frombuffer(in_data, dtype=np.int16) # Convert the input data to a NumPy array
    
    # *this is the max data of the amplitude got from the numpy array
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data)) #*updates the progress bar according to the sound density

    freqs = np.fft.fftfreq(len(data), d=1/RATE)
    fft = np.fft.fft(data)
    index = np.argmax(np.abs(fft))
    freq = freqs[index]
    _VARS['window']['Frequency'].update(f'{freq:.2f} Hz')
        
    
    

    rms = np.sqrt(np.mean(np.square(data)))
    _VARS['window']['-Amplitude-'].update(f'{rms:.2f} dB')
    print(f'{rms:.2f} dB')

    
    

    
    # returning the data
    return (in_data, pyaudio.paContinue)


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

    #!reading the whole audio stream data and saving it using loop

    
    
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
        
# clsoe the window UI anyway after the loop
_VARS['window'].close()