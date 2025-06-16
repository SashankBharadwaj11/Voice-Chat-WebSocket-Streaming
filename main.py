import asyncio

from audio.vad_recorder import record_audio_with_vad
from stt.whisper_transcriber import transcribe_audio
from llm.openrouter_client import get_llm_response, build_prompt 
from tts.resemble_tts import stream_tts_ws 

# pipeline configurations
PIPELINES = {
    "en-en": {
        "voice_uuid": "ae8223ca",
        "language": "en",
        "prompt_type": "english"
    },
    "en-jp": {
        "voice_uuid": "e5d4a1d6",
        "language": "ja",
        "prompt_type": "japanese"
    }
}

def choose_pipeline():
    print("\n🌐 Choose language pipeline:")
    print("1. English → English")
    print("2. English → Japanese")
    choice = input("Enter 1 or 2: ").strip()
    return "en-en" if choice == "1" else "en-jp"

# Main loop
async def voice_assistant_loop(pipeline_key: str):
    pipeline = PIPELINES[pipeline_key]
    print(f"🟢 Voice Assistant Running [{pipeline_key}]...\n")

    while True:
        try:
            # Step 1: Record with VAD
            input_path = record_audio_with_vad()

            # Step 2: Transcribe with Whisper
            user_text = transcribe_audio(input_path)
            if not user_text.strip():
                print("No speech detected. Listening again...\n")
                continue

            print(f"🗣️ You said: {user_text}")

            # Step 3: Build prompt & get LLM response
            prompt = build_prompt(user_text, pipeline["prompt_type"])
            llm_response = get_llm_response(prompt)
            print("🤖 Assistant:", llm_response)

            # Step 4: Speak the response using pipeline specific voice, lang
            await stream_tts_ws(llm_response, voice_uuid=pipeline["voice_uuid"], language=pipeline["language"])

        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}\n")
            continue

# Entry point
if __name__ == "__main__":
    print("🟢 Voice Assistant Started")
    selected_pipeline = choose_pipeline()
    asyncio.run(voice_assistant_loop(selected_pipeline))
