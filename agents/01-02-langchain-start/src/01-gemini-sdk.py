import os

# Estas variables de entorno las usamos para que las salidas a la consola
# se vean más limpias, pero no afecta la funcionalidad de tu aplicación
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_LOG_SEVERITY_LEVEL"] = "ERROR"

from dotenv import load_dotenv
import google.generativeai as genai

# Cargar archivo .env
load_dotenv()

# Recupera el API Key del archivo env
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Crear una referencia al modelo
model = genai.GenerativeModel("gemini-2.5-flash-lite")

print("=" * 80)
print("EJEMPLO 1: Gemini SDK (SIN MEMORIA)")
print("=" * 80)

# Primera pregunta
response1 = model.generate_content("Cuál es la capital de Italia")
print("Usuario: Cuál es la capital de Italia")
print(f"Gemini: {response1.text}\n")

# Segunda pregunta - Nota: No tiene contexto de la conversación anterior
response2 = model.generate_content("¿qué lugares me aconsejas para visitar ahí?")
print("Usuario: ¿qué lugares me aconsejas para visitar ahí?")
print(f"Gemini: {response2.text}")
print("\n⚠️  Observa que Gemini NO sabe que 'ahí' se refiere a Roma")
print("=" * 80)
