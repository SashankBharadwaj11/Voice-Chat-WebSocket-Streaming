import simpleaudio as sa
import os

def play_audio(file_path):
    print(f"🔊 Trying to play: {file_path}")
    if not os.path.exists(file_path):
        print("File not found!")
        return
    try:
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        print("Playing audio...")
        play_obj.wait_done()
        print("Playback finished.")
    except Exception as e:
        print(f"Playback failed: {e}")
