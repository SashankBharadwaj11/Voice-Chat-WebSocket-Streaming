import asyncio
import base64
import json
import websockets
import pyaudio

RESEMBLE_API_KEY = "QPGfA2Y3Qe5qP5uYgyjN4Att"
WS_URL = "wss://websocket.cluster.resemble.ai/stream"

# TTS stream function
async def stream_tts_ws(text: str, voice_uuid: str, language: str = "en"):
    headers = {
        "Authorization": f"Token {RESEMBLE_API_KEY}"
    }

    async with websockets.connect(WS_URL, extra_headers=headers) as ws:
        # synthesis request
        request = {
            "voice_uuid": voice_uuid,
            "data": text,
            "binary_response": False,
            "output_format": "wav",
            "sample_rate": 22050,
            "precision": "PCM_16",
            "language": language 
        }

        await ws.send(json.dumps(request))
        print(f"🔁 Streaming TTS from Resemble (lang: {language})...")

        # Audio stream setup
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=22050, output=True)

        try:
            while True:
                message = await ws.recv()
                data = json.loads(message)

                if data["type"] == "audio":
                    audio_b64 = data["audio_content"]
                    audio_bytes = base64.b64decode(audio_b64)
                    stream.write(audio_bytes)

                elif data["type"] == "audio_end":
                    print("✅ Playback finished.")
                    break

                elif data["type"] == "error":
                    print(f"Error: {data['message']}")
                    break

        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()

# sync starter for testing
def start_streaming_tts(text: str, voice_uuid: str, language: str = "en"):
    asyncio.run(stream_tts_ws(text, voice_uuid, language))
