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

print("\n\n" + "=" * 80)
print("EJEMPLO 2: OpenAI SDK (SIN MEMORIA)")
print("=" * 80)

# Primera pregunta
response1 = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Cuál es la capital de Italia"}],
)
print("Usuario: Cuál es la capital de Italia")
print(f"OpenAI: {response1.choices[0].message.content}\n")

# Segunda pregunta - Nota: No tiene contexto de la conversación anterior
response2 = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "¿qué lugares me aconsejas para visitar ahí?"}
    ],
)
print("Usuario: ¿qué lugares me aconsejas para visitar ahí?")
print(f"OpenAI: {response2.choices[0].message.content}")
print("\n⚠️  Observa que OpenAI NO sabe que 'ahí' se refiere a Roma")
print("=" * 80)
