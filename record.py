#!/usr/bin/env python3
import time

import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self,lang='es-ES', ambient_duration=2):
        self.recognizer = sr.Recognizer()
        self.lang = lang
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            t = time.time()
            #lang 
            #    -"english"
            text = self.recognizer.recognize_google(audio, language=self.lang)
            #text = self.recognizer.recognize_whisper(audio, language="english", model=model)
            time_parsing = time.time() - t
            if time_parsing > 2:
                print(f"Recognized in {time.time() - t} seconds - maybe try again. ")

            return text

        except sr.UnknownValueError:
            print("i'm sorry but i could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper")
