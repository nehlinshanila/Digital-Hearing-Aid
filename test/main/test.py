import pyaudio
import numpy as np
import PySimpleGUI as sg

freq_bins = 1
psd= 1

# Define the PyAudio callback function
def audio_callback(in_data, frame_count, time_info, status):
    # Convert the input data to a NumPy array
    data = np.frombuffer(in_data, dtype=np.float32)

    # Calculate the FFT of the data
    fft_data = np.fft.fft(data)

    # Calculate the power spectral density (PSD) of the data
    psd = np.abs(fft_data) ** 2

    # Calculate the frequency bins for the PSD
    freq_bins = np.fft.fftfreq(len(psd)) * sample_rate

    # Find the peak frequency in the PSD
    peak_idx = np.argmax(psd)
    peak_freq = freq_bins[peak_idx]

    # Update the frequency display on the GUI
    window['-FREQ-'].update(f'Peak frequency: {peak_freq:.2f} Hz')

    return (in_data, pyaudio.paContinue)

# Create the PyAudio object
p = pyaudio.PyAudio()

# Set up the audio stream with the callback function
sample_rate = 44100
buffer_size = 1024
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=buffer_size,
                stream_callback=audio_callback)

# Create the PySimpleGUI window
layout = [[sg.Canvas(size=(400, 300), key='-CANVAS-')],
          [sg.Text('Peak frequency: 0 Hz', key='-FREQ-')]]
window = sg.Window('Real-time frequency display', layout)

# Set up the plot for the frequency data
canvas = window['-CANVAS-'].TKCanvas
line = canvas.create_line((0, 150, 400, 150), fill='red', width=2)

# Start the audio stream
stream.start_stream()

# Main event loop
while True:
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED:
        break

    # Update the plot with the latest frequency data
    canvas.delete(line)
    line = canvas.create_line([(freq_bins[i], 300 - 10 * np.log10(psd[i]))
                               for i in range(len(psd) // 2)],
                              fill='red', width=2)

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
window.close()
