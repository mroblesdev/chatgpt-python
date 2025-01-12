# Importamos el cliente OpenAI desde la biblioteca instalada (pip install openai).
from openai import OpenAI

# Creamos una instancia del cliente de OpenAI.
# Asegúrate de reemplazar "TU_API_KEY" con tu clave válida de OpenAI.
client = OpenAI(api_key="TU_API_KEY")

# Usamos el cliente para realizar una solicitud de completado en el modelo "gpt-4o-mini".
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
       {"role": "user", "content": "Que es python?"}
    ],
    max_completion_tokens=100 # Limitamos la cantidad máxima de tokens en la respuesta.
)

# Imprimimos el contenido de la respuesta del modelo.
print(completion.choices[0].message.content)
