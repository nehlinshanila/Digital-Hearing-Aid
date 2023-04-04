samples = np.frombuffer(data, dtype=np.float32)
    # calculate root-mean-square (RMS) amplitude of samples
    rms = np.sqrt(np.mean(samples**2))