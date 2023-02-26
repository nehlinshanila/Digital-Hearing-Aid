import PySimpleGUI as sg #for the UI design
import pyaudio #for the input of the audio
import numpy as np #for numeric and mathematical calculations such as fast fourier transformation(fft)

"""PyAudio PySimpleGUI Non Blocking Stream for Microphone"""

# VARS contants that will control the window's UI and the UI of the Audio stream
_VARS = {'window': False,
         'stream': False,
        #  'canvas': False
         }

# pysimpleGUI initiation
# here we initiate the overall UI and then control afterwards
AppFont = 'Any 16'
# the theme of the UI
sg.theme('DarkTeal2')

# this here customizes the layout
layout = [[sg.ProgressBar(4000, orientation='h',
                          size=(20, 20), key='-PROG-')],
          [sg.Text('Frequency: ', font=AppFont),
           sg.Text('0 Hz', key='Frequency',font=AppFont)],
          [sg.Button('Listen', key='Listen', font=AppFont),
           sg.Button('Stop', key='Stop', font=AppFont, disabled=True),
           sg.Button('Exit', key='Exit', font=AppFont)],
        #   [sg.Text('Frequency:', font=AppFont),
        #    sg.Canvas(key='-CANVAS-'),
        #    sg.Text('Peak Frequency', font=AppFont, key='-FREQ-')]
          ]

# finalizing the window UI
_VARS['window'] = sg.Window('Microphone Level', layout, finalize=True)


# canvas = _VARS['window']['-CANVAS-'].TKCanvas
# line = canvas.create_line((0, 150, 400, 150), fill='red', width=2)

# initiating constants for the audio stream data
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 22000  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen
CHANNELS = 1
freq_binary = None
psd = None

# PyAudio initiation
pAud = pyaudio.PyAudio()



# FUNCTIONS:

# this controls the stop button of the UI
def stop():
    if _VARS['stream']:
        _VARS['stream'].stop_stream()
        _VARS['stream'].close()
        _VARS['window']['-PROG-'].update(0)
        _VARS['window']['Stop'].Update(disabled=True)
        _VARS['window']['Listen'].Update(disabled=False)
        _VARS['window']['Frequency'].Update('0 Hz')

# returns the data extracted from the audio input
def callback(in_data, frame_count, time_info, status):
    # this is the input data or audio stream
    # print(in_data)
    data = np.frombuffer(in_data, dtype=np.int16)
    # print(data)
    data2 = np.frombuffer(data, dtype=np.float32)
    # print(data2)
    fft_data = np.fft.fft(data)
    # print(fft_data)
    psd = np.abs(fft_data) ** 2
    # print(psd)
    freq_binary = np.fft.fftfreq(len(psd)) * RATE
    # print(freq_binary)
    peak_idx = np.argmax(psd)
    # print(peak_idx)
    peak_freq = freq_binary[peak_idx]
    # print(peak_freq)
    
    # this is the max data of the amplitude
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data))
    
    # data = in_data.read(CHUNK)
    # elapsed_time = len(in_data) / (RATE * CHANNELS * 2)
    # frecuency = (2 * np.pi * elapsed_time * RATE) / CHUNK
    
    # print(peak_freq)
    _VARS['window']['Frequency'].update(f'{peak_freq} Hz')
    
    
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
                                frames_per_buffer=CHUNK,
                                stream_callback=callback)

    _VARS['stream'].start_stream()
    
# This is where the main loop happens
# it's an infinite loop and it only stops when stop button is pressed
# or the window is closed
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
        
    # canvas.delete(line)
    # line = canvas.create_line([(freq_binary[i], 300 -10 * np.log10(psd[i]))
    #                            for i in range(len(psd) //2)], 
    #                           fill='red', width=2)

# clsoe the window UI anyway after the loop
_VARS['window'].close()