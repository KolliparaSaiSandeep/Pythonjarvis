import os
from datetime import timedelta
from datetime import datetime

import pywhatkit
from bs4 import BeautifulSoup
import pyttsx3
import requests
import speech_recognition
import greetme

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        speech_recognition.Recognizer().adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=3)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            return "None"
        return query
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91000000000",message,time_hour=strTime,time_min=update)
    elif a==2:
        pass