from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

async def send_voice_reply(to: str, audio_path: str):
    try:
        # Primero subimos el archivo de audio a algún hosting público
        # Para este ejemplo, debes subirlo manualmente o usar un CDN/S3
        # Aquí va un ejemplo temporal con archivo local convertido a enlace público
        # Reemplázalo con la URL real de tu archivo
        public_url = upload_to_somewhere(audio_path)  # FUNCIONALIDAD A IMPLEMENTAR

        message = client.messages.create(
            from_='whatsapp:' + TWILIO_PHONE_NUMBER,
            to=to,
            media_url=[public_url]
        )
        print(f"[Twilio] Mensaje enviado a {to}")
    except Exception as e:
        print(f"[Twilio] Error enviando audio: {e}")

# 👇 Implementación temporal
def upload_to_somewhere(audio_path: str) -> str:
    # 🔧 TEMPORAL: necesitas alojar el archivo en un servidor público
    # Puedes usar:
    # - S3 de AWS
    # - Cloudinary
    # - Bunny.net
    # - Google Cloud Storage
    # Aquí debes devolver la URL pública al archivo mp3

    print(f"[Upload] 🔧 Sube manualmente este archivo: {audio_path}")
    return "https://tuservidor.com/audio/" + os.path.basename(audio_path)
