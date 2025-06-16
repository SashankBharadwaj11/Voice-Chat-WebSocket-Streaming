import os
import whisper

def transcribe_audio(audio_path):
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) < 1000:
        raise ValueError("Transcription failed: audio file is empty or corrupted")

    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"].strip()
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")
