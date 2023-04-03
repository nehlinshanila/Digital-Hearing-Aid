import numpy as np
import sounddevice as sd

# Define a scaling factor for the audio input
scaling_factor = 0.5

# Define a callback function to modify the audio input
def audio_callback(indata, frames, time, status):
    # Check if the audio input is valid
    if status:
        print(status, flush=True)
    # Modify the audio input by scaling the audio signal
    indata *= scaling_factor
    # Play the modified audio input
    sd.play(indata)

# Start the audio input stream with the modified audio callback function
with sd.InputStream(callback=audio_callback):
    sd.sleep(10000)
