import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
import time

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5 
THRESHOLD = 0.005 

def record_audio_with_vad():
    recording = []

    def callback(indata, frames, time_info, status):
        volume = np.linalg.norm(indata) / len(indata)
        recording.extend(indata.copy())

    try:
        with sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE):
            sd.sleep(DURATION * 1000)
    except Exception as e:
        raise RuntimeError(f"Mic error: {e}")

    os.makedirs("tmp", exist_ok=True)
    file_path = f"tmp/debug_{int(time.time())}.wav"
    write(file_path, SAMPLE_RATE, np.array(recording))
    return file_path
