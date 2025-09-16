import os
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = (
    "***REMOVED***"
)


llm = OpenAI(temperature=0.9)  # 0 is less creativity, 1 is maximum creativity

prompt = "Di 'hola mundo desde langchain' en el idioma de tu preferencia, y luego dime, en español, en qué idioma fue el saludo"

print(llm.invoke(prompt))  
