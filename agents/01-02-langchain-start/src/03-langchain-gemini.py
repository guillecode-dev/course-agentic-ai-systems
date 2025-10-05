from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

print("\n\n" + "=" * 80)
print("EJEMPLO 3: Gemini con Langchain (CON MEMORIA)")
print("=" * 80)

# Configurar el modelo
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", google_api_key="TU_GEMINI_API_KEY", temperature=0.7
)

# Crear memoria de conversación
memory = ConversationBufferMemory()

# Crear cadena de conversación
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

# Primera pregunta
response1 = conversation.predict(input="Cuál es la capital de Italia")
print("Usuario: Cuál es la capital de Italia")
print(f"Gemini: {response1}\n")

# Segunda pregunta - Tiene contexto de la conversación
response2 = conversation.predict(input="¿qué lugares me aconsejas para visitar ahí?")
print("Usuario: ¿qué lugares me aconsejas para visitar ahí?")
print(f"Gemini: {response2}")
print("\n✅ Observa que Gemini SÍ sabe que 'ahí' se refiere a Roma")
print("=" * 80)
