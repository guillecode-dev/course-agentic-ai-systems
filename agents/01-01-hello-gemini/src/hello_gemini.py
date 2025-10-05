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

# Envía un prompt sencillo
response = model.generate_content(
    "Di 'hola mundo desde Gemini' en un idioma al azar y a continuación indica en español en qué idioma fue el saludo."
)

# Imprimir respuesta
print(response.text.strip())
