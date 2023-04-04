import sounddevice as sd

print(sd.query_devices())
supported_formats = sd.query_hostapis()
print("Supported input formats:", supported_formats['input'])
print("Supported output formats:", supported_formats['output'])