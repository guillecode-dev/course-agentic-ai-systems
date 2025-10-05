import os
from dotenv import load_dotenv
import openai

# Cargar archivo .env
load_dotenv()

# Obtiene API Key y ProjectID de archivo .env
api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_API_PROJECT_ID")

openai.api_key = api_key
openai.api_base = os.getenv("OPENAI_API_BASE")

# Usando la API de completions para enviar un prompt sencillo
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role": "user",
            "content": "Di 'hola mundo desde OpenAI' en el idioma de tu preferencia y a continuación indica en español en qué idioma fue el saludo",
        },
    ],
)

print(response.choices[0].message.content.strip())
