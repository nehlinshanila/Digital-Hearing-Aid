import PySimpleGUI as sg #for the UI design
import pyaudio #for the input of the audio
import numpy as np #for numaric and mathematical calculationssuch as fourier

"""PyAudio PySimpleGUI Non Blocking Stream for Microphone"""

# VARS contants that will control the window's UI and the UI of the Audio stream
_VARS = {'window': False,
         'stream': False}

# pysimpleGUI initiation
# here we initiate the overall UI and then control afterwards
AppFont = 'Any 16'
# the theme of the UI
sg.theme('DarkTeal2')

# this here customizes the layout
layout = [[sg.ProgressBar(4000, orientation='h',
                          size=(20, 20), key='-PROG-')],
          [sg.Button('Listen', font=AppFont),
           sg.Button('Stop', font=AppFont, disabled=True),
           sg.Button('Exit', font=AppFont)]]

# finalizing the window UI
_VARS['window'] = sg.Window('Microphone Level', layout, finalize=True)

# initiating constants for the audio stream data
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen

# PyAudio initiation
pAud = pyaudio.PyAudio()



# FUNCTIONS:

# this controls the stop button of the UI
def stop():
    if _VARS['stream']:
        _VARS['stream'].stop_stream()
        _VARS['stream'].close()
        _VARS['window']['-PROG-'].update(0)
        _VARS['window'].FindElement('Stop').Update(disabled=True)
        _VARS['window'].FindElement('Listen').Update(disabled=False)

# returns the data extracted from the audio input
def callback(in_data, frame_count, time_info, status):
    # this is the input data or audio stream
    # print(in_data)
    data = np.frombuffer(in_data, dtype=np.int16)
    
    # this is the max data of the amplitude
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data))

    # returning the data
    return (in_data, pyaudio.paContinue)


# this function controls the listen button of the UI
def listen():
    _VARS['window'].FindElement('Stop').Update(disabled=False)
    _VARS['window'].FindElement('Listen').Update(disabled=True)
    # this part enables the audio input
    # here we can talk using the microphone
    _VARS['stream'] = pAud.open(format=pyaudio.paInt16,
                                channels=1,
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

# clsoe the window UI anyway after the loop
_VARS['window'].close()