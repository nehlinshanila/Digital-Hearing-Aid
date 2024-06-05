import struct
import pyaudio #for the input of the audio
import numpy as np #for numaric and mathematical calculationssuch as fourier
import math
from scipy import signal


limiter_gain = 1.0
limiter_threshold_value = 0.9
amplification_factor = 8
amplification_factor_lower_bound = 2
amplification_factor_upper_bound = 4

cutoff_frequency = 1800
loud_check_threshold = 0.4


CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 48000  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds. ie, Interval to listen
CHANNELS = 1
freq_bins = None
psd = None
start = 0.00
end = 0.00
elapsed_time = 0.00

FORMAT = pyaudio.paInt16

frames = []

pAud = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):

    data = np.frombuffer(in_data, dtype=np.int16) # Convert the input data to a NumPy array
    
    loud_check_value =np.abs(np.sqrt(np.mean(np.square(data/32767))))

    if loud_check_value > loud_check_threshold:
        amplification_factor = amplification_factor_lower_bound
    else:
        amplification_factor = amplification_factor_lower_bound
        
    #? the amplification
    samples = list(struct.unpack(f"{frame_count}h", in_data))
    
     # Apply a low-pass filter to the incoming audio data
    normalized_cutoff_frequency = 2 * cutoff_frequency / RATE
    b, a = signal.butter(5, normalized_cutoff_frequency, "low")
    filtered_samples = signal.lfilter(b, a, samples)

    # Apply a limiter to prevent clipping
    limiter_threshold = limiter_threshold_value * 32767
    for i in range(len(filtered_samples)):
        if filtered_samples[i] > limiter_threshold:
            limiter_gain = 1.0 + ((32767 - filtered_samples[i]) / 32767)  # Adjust this formula as needed

            filtered_samples[i] = math.floor(limiter_threshold + (filtered_samples[i] - limiter_threshold) * limiter_gain)

    # Amplify the audio by a factor of amplification_factor

    amplified_data = [max(min(int(sample * amplification_factor), 32767), -32768) for sample in filtered_samples]
    # Convert the amplified data back to bytes
    return (struct.pack(f"<{frame_count}h", *amplified_data), pyaudio.paContinue)



stream = pAud.open(format = pyaudio.paInt16,
                                channels = CHANNELS,
                                rate = RATE,
                                input = True,
                                output = True,
                                frames_per_buffer = CHUNK,
                                stream_callback = callback)

# *starts the audio stream

if __name__ == "__main__":
    while True:
        stream.start_stream()
    
stream.stop_stream()
stream.close()
stream.terminate()
