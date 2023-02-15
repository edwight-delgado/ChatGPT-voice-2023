# GPT asistente 2023

**GPT asistente** es un asistente de voz que aprovecha el potente chatbot ChatGPT de [openai](https://openai.com/) para responder a sus preguntas. Es tan sencillo que usted le hable y GPT asistente responde con voz humana.

## Lista de materiales

- 1 Orange pi 4 o Raspberry pi 4
- 1 x micrófono USB o Jack
- 1 altavoz

## Cómo funciona

Para alojar el proyecto utilicé un Orange Pi 4, porque ejecuta Linux y ofrece mucha versatilidad. Y es muy potente para su pequeño tamaño. El script recopila el audio de la voz de un hablante mediante el micrófono. Luego, se usa la librería **speech_recognition** para convertir ese archivo de audio en texto. Luego, el texto se consulta en ChatGPT mediante una [API no oficial] (https://github.com/acheong08/ChatGPT-lite) que devuelve una cadena de texto de la respuesta de ChatGPT. Esa respuesta luego es procesada por **gtts** para convertirla en voz humana que la Orange Pi puede reproducir a través de un altavoz.

## Instalación 
- Crear un ambiente virtual
 ```sh
	python3 -m venv venv
 ```
- Activar el ambiente en bash
```sh
	source venv/bin/activate 
```
- activar el ambiente con fish
```sh
	source venv/bin/activate.fish 
```
- instalar los paquetes y librerías necesarias 
```sh
	pip install requirements.txt 
```

- renombrar .env.example a .env cambiar el token en el archivo por el de la página de ChatGPT
```env
	token_key = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.."
```

## donde obtengo el token 
En la página de [https://chat.openai.com/chat](https://chat.openai.com/chat) copias el auth-session-token y lo copias en el archivo .env

## Cómo se usa
Ejecuta el siguiente script
```sh
    python voice_chat.py
```

Él responderá con

  Hola. En que puedo ayudarte.

Seguido de 2 segundos planteas tu pregunta 

Ejemplo "¿qué películas  de terror me recomiendas para este fin de semana?"

Si todo está bien recibirás la repuesta en unos pocos segundos, en formato audio 

para detener simplemente di **adiós** puede ser una frase como **gracias por todo y adiós **



## Referencias y Créditos 
Este prototipo está derivado del proyecto
[Nick A. Bild, MS](https://github.com/nickbild/voice_chatgpt)
[Antonio Cheong] (https://github.com/acheong08/ChatGPT-lite)

