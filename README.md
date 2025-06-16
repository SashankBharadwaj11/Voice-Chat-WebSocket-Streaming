# Streaming Voice AI Assistant (English & Japanese)

An end-to-end AI voice assistant that listens to your voice, transcribes it in real-time using WhisperX with Voice Activity Detection (VAD), sends it to a streaming LLM via OpenRouter (e.g., Gemma 12B/27B), and speaks the response naturally using Resemble AI’s WebSocket Text-to-Speech (TTS). The system is designed to be conversational, fast (sub-2-second latency), and support **multilingual output** including **English and Japanese**.

---

## Tech Stack

| Component       | Technology                     |
|----------------|---------------------------------|
| STT         | WhisperX + VAD (Voice Activity Detection) |
| LLM         | Google Gemma 12B / 27B via OpenRouter (Streaming) |
| TTS         | Resemble AI (WebSocket Streaming TTS) |
| Framework    | Python 3.10+, SoundDevice, PyAudio |
| Language     | English 🇺🇸 + Japanese 🇯🇵 |

---

## Features

- **Real-time latency**: Sub-2 seconds roundtrip
- **Modular pipeline**: STT → LLM → TTS in one script
- **Streaming LLM**: Generates response tokens on the fly
- **Streaming TTS**: Starts speaking before LLM finishes
- **Multilingual**: Fluent English & Japanese (prompt-controlled)

---

## Installation & Setup

Python 3.10 (recommended)
> - Microsoft C++ Build Tools (required for WhisperX and PyAudio)
> - Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
> - FFmpeg (for Whisper-based audio processing)


1. Clone the Repository
git clone https://github.com/your-username/streaming-voice-ai.git
cd streaming-voice-ai

2. Create Python Virtual Environment and Activate It
python -m venv venv
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

3. Install All Required Python Packages
Contents of requirements.txt:
openai-whisper
whisperx
httpx
pyaudio
websockets
numpy
sounddevice
scipy
python-dotenv

4. Environment Variable Setup
OPENROUTER_API_KEY=your_openrouter_key_here
RESEMBLE_API_KEY=your_resemble_token_here
VOICE_UUID=your_voice_uuid_here

5. How to Run
python voice_assistant.py
The assistant will:
Automatically detect when you start speaking (via VAD)
Transcribe your voice using WhisperX
Generate a response using OpenRouter (LLM)
Speak it in real-time via Resemble AI streaming TTS

6. Sample Output
📝 Transcribed: What is AI?
🤖 LLM: <speak>Artificial Intelligence <break time="200ms"/> is the ability of machines to mimic human thinking.</speak>
🗣️ Spoken by Resemble in real-time


👨‍💻 Author
Made with ❤️ by Lokesh 
Built for real-time voice interactions using open-source models.
Supports both English and Japanese.

