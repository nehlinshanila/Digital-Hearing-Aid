import pyaudio
import numpy as np
import time
import struct
from scipy import signal

# all the variables
# how much the audio data needs to gain
limiter_gain = 1.0 # the gain value
limiter_threshold_value = 0.9 # the threshold value
# how much the sounds need amplifying
amplification_factor = 8 #main factor
amplification_factor_lower_bound = 2 #lower bound
amplification_factor_upper_bound = 4 #Upper bound
# the the frequency that needs to be cutoff
cutoff_frequency = 3200
# loudness check for comfortable hearinng
loud_check_threshold = 65


CHUNK = 1024  # Samples: 2048, 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz (44100 or 48000)
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen
CHANNELS = 1  # audio input devices
FORMAT = pyaudio.paInt16 # data formatting type

def is_loud(data):
    
    loud_check_value = np.abs(np.sqrt(np.mean(np.square(data))))
    
    if loud_check_value > loud_check_threshold:
        factor = amplification_factor_lower_bound
    else:
        factor = amplification_factor_upper_bound
            
    return factor

def low_pass_filter_data(in_data, frame_count):
    
    samples = list(struct.unpack(f"{frame_count}h", in_data))
    
     # Apply a low-pass filter to the incoming audio data
    normalized_cutoff_frequency = 2 * cutoff_frequency / RATE
    b, a = signal.butter(5, normalized_cutoff_frequency, "low")
    
    filtered_samples = signal.lfilter(b, a, samples)
    
    filtered_samples = np.array(filtered_samples)
    
    return filtered_samples

def amplify_data(filtered_samples, limiter_threshold):
    # Apply a limiter to the audio data.
    limiter_gain = np.clip((32767 - filtered_samples) / 32767, 0, 1)
    filtered_samples = np.clip(limiter_threshold + (filtered_samples - limiter_threshold) * limiter_gain, 0, 32767)

    # Amplify the audio by a factor of amplification_factor.
    amplified_data = np.clip(filtered_samples * amplification_factor, -32768, 32767)

    return amplified_data.astype(np.int64)

def callback(in_data, frame_count, time_info, status):
    # converts the incoming sound data into a int116 numpy array
    data = np.frombuffer(in_data, dtype=np.int16)
    
    #to check the loudness of the audio data
    amplification_factor = is_loud(data)
         
    filtered_samples = low_pass_filter_data(in_data, frame_count)

    # Apply a limiter to prevent clipping
    limiter_threshold = limiter_threshold_value * 32767
    
    amplified_data = amplify_data(filtered_samples, limiter_threshold)
    # Convert the amplified data back to bytes
    return (struct.pack(f"<{frame_count}h", *amplified_data), pyaudio.paContinue)


def main():
    # Create a PyAudio object.
    p = pyaudio.PyAudio()

    # Open a stream for input.
    stream = p.open(format=FORMAT, 
                    channels=1, 
                    rate=RATE, 
                    frames_per_buffer = CHUNK, 
                    input=True, output=True, 
                    stream_callback=callback)

    # Start the stream.
    stream.start_stream()

    # Wait for the stream to stop.
    while stream.is_active():
        time.sleep(0.01)

    # for stopping the stream
    # stream.stop_stream()
    
    # Close the stream.
    stream.close()

    # Close the PyAudio object.
    p.terminate()

if __name__ == "__main__":
    main()
