import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def translate_text(text: str) -> str:
    try:
        system_prompt = (
            "Eres un traductor profesional. Si el texto está en español, tradúcelo al inglés. "
            "Si está en inglés, tradúcelo al español. Devuelve solo la traducción, sin explicaciones."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )

        translation = response["choices"][0]["message"]["content"].strip()
        print(f"[GPT] Traducción: {translation}")
        return translation
    except Exception as e:
        print(f"[GPT] Error: {e}")
        return "Lo siento, no pude traducir el texto."
