# Chat con OpenAI API

Este repositorio contiene dos scripts en Python que implementan un sistema de chat utilizando la API de OpenAI. Los scripts permiten interactuar con un modelo de lenguaje (GPT-4o-mini) de manera dinámica.

## Requisitos

Antes de ejecutar los scripts, asegúrate de tener instalados los siguientes elementos:

- Python 3.7 o superior.
- Biblioteca `openai` instalada. Puedes instalarla con:
  ```bash
  pip install openai
  ```

## Configuración

Para usar los scripts, necesitas una clave de API válida de OpenAI. 

```bash
client = OpenAI(api_key="TU_API_KEY")
```

## Scripts

### 1. **`basico.py`**

Este script realiza una consulta simple al modelo GPT-4o-mini y muestra la respuesta en la terminal.

**Uso:**
```bash
python basico.py
```

**Flujo del script:**
- Envía una pregunta definida al modelo.
- Muestra la respuesta generada.

---

### 2. **`chat.py`**

Este script implementa un sistema de chat interactivo donde puedes enviar múltiples mensajes y recibir respuestas del modelo.

**Uso:**
```bash
python chat.py
```

**Flujo del script:**
- Escribe tu mensaje en la consola.
- Recibe una respuesta del modelo.
- Escribe "salir", "exit" o "quit" para finalizar el programa.

---

## Ejemplo de Ejecución

### Script Básico:
```bash
Tú: ¿Qué es Python?
Asistente: Python es un lenguaje de programación...
```

### Chat Interactivo:
```bash
Tú: Hola
Asistente: ¡Hola! ¿En qué puedo ayudarte?

Tú: ¿Qué es Python?
Asistente: Python es un lenguaje de programación...

Tú: salir
Asistente: Bye!
```

## Contribución

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o pull request para mejoras.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invitame una cerveza 🍺 o un café ☕ [Da clic aquí](https://www.paypal.com/paypalme/markorobles?locale.x=es_XC.).
- Da las gracias públicamente 🤓.
