# Importamos el cliente OpenAI desde la biblioteca instalada (pip install openai).
from openai import OpenAI

# Creamos una instancia del cliente de OpenAI.
# Asegúrate de reemplazar "TU_API_KEY" con tu clave válida de OpenAI.
client = OpenAI(api_key="TU_API_KEY")

# Inicializamos una lista para almacenar el historial de mensajes de la conversación.
messages = []

while True:
    user_input = input("Tú: ")
    
    # Verificamos si el usuario desea salir del programa.
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Asistente: Bye!")
        break

    # Agregamos el mensaje del usuario al historial de la conversación.
    messages.append({"role": "user", "content": user_input})

    # Realizamos una solicitud al modelo para generar una respuesta.
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=messages,
        max_completion_tokens=100
    )

    # Imprimimos la respuesta generada por el modelo.
    print(completion.choices[0].message)
    
    # Agregamos la respuesta del asistente al historial de la conversación.
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
