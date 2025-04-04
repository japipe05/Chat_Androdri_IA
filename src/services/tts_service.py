from google.cloud import texttospeech
import os
import uuid

# Se asegura de que la variable esté activa para Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

async def text_to_speech(text: str) -> str:
    try:
        client = texttospeech.TextToSpeechClient()

        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Puedes personalizar idioma y voz aquí
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US" if is_english(text) else "es-ES",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        output_path = f"audio_reply_{uuid.uuid4().hex}.mp3"
        with open(output_path, "wb") as out:
            out.write(response.audio_content)

        print(f"[TTS] Audio generado: {output_path}")
        return output_path

    except Exception as e:
        print(f"[TTS] Error: {e}")
        return None

def is_english(text: str) -> bool:
    # Detección simple (puedes mejorar con langdetect si quieres)
    return all(ord(c) < 128 for c in text)
