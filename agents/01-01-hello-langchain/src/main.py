import os
from dotenv import load_dotenv
import openai

# Cargar .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_API_PROJECT_ID")

openai.api_key = api_key
openai.api_base = os.getenv("OPENAI_API_BASE")

# Usando la nueva API de completions
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {
            "role": "user",
            "content": "Di 'hola mundo desde OpenAI' en el idioma de tu preferencia y a continuación indica en español en qué idioma fue el saludo",
        },
    ],
)

print(response.choices[0].message.content.strip())
