################################################################
# Nick Bild
# January 2023
# https://github.com/nickbild/voice_chatgpt
#
# Voice-controlled ChatGPT prompt
################################################################

from record import SpeechRecognizer
from speak import Talk
from ChatGpt import MyChatGPT

from dotenv import dotenv_values,load_dotenv
import wikipedia
from unicodedata import normalize
from time import sleep

def text_normalize(prompt):
    if prompt != None:
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        n = normalize('NFKC', normalize('NFKD', prompt).translate(trans_tab))
        return n.lower()
    else:
        main()

check = load_dotenv('.env')
if check == True:
    env = dotenv_values(".env")
else:
    print('no se encuentra archivo el .env')



def hello(speak):
    speak.speak("Hola. En que puedo ayudarte.")



def main(lang='es'):
    listen = SpeechRecognizer(lang=lang)
    speak = Talk(lang)
    wikipedia.set_lang(lang)


    # Get WAV from microphone.
    # Convert audio into text.
    hello(speak)
    
    while True:
        print('escuchando...')
        question = listen.listen()
        question = text_normalize(question)
        # Convert audio into text.

        
        # Send text to ChatGPT.
        print("Asking: {0}".format(question))
        if "busca en google" in question:
            speak("buscando en Google ")
            continue

        elif "busca en wikipedia" in question:
             
            # if any one wants to have a information
            # from wikipedia
            speak.speak("buscando en wikipedia ")
            question = question.replace("wikipedia", "")
             
            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(question, sentences=4)
            speak.speak("de acuerdo a wikipedia")
            speak.speak(result)
            continue
        
        elif "gpt" in question:
            chat = MyChatGPT(env)
            gpt_response = chat.ask(question)
            print("Response: {0}".format(gpt_response))
            speak.speak(gpt_response)
            chat.close()
            #asyncio.coroutine(ask_chat_gpt(env, question))
            #speak.speak(gpt_response)
            continue
            

        elif "adios" in question:
            speak.speak("Es un placer para mi ayudarte.")
            sleep(3)
            exit()


    

if __name__ == "__main__":
    main()

