from fastapi import FastAPI, Request, Form
from services.whisper_service import transcribe_audio
from services.translation_service import translate_text
from services.tts_service import text_to_speech
from services.twilio_service import send_voice_reply
import os
import httpx

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(
    request: Request,
    MediaUrl0: str = Form(None),
    From: str = Form(...),
    Body: str = Form("")
):
    if MediaUrl0:  # Si hay audio
        # 1. Descargar audio
        async with httpx.AsyncClient() as client:
            response = await client.get(MediaUrl0)
            audio_data = response.content
            audio_path = "temp_audio.ogg"
            with open(audio_path, "wb") as f:
                f.write(audio_data)

        # 2. Transcribir con Whisper
        transcript = await transcribe_audio(audio_path)

        # 3. Traducir texto
        translated_text = await translate_text(transcript)

        # 4. Convertir texto a audio
        audio_reply_path = await text_to_speech(translated_text)

        # 5. Enviar respuesta por WhatsApp
        await send_voice_reply(From, audio_reply_path)

        return {"status": "ok", "message": translated_text}

    return {"message": "No audio received"}
