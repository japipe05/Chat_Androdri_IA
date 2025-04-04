import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def transcribe_audio(audio_path: str) -> str:
    try:
        with open(audio_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        print(f"[Whisper] Transcripción: {response}")
        return response.strip()
    except Exception as e:
        print(f"[Whisper] Error: {e}")
        return "Lo siento, no pude transcribir el audio."
