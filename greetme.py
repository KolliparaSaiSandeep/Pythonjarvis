import datetime
from datetime import datetime
import pyttsx3
import speech_recognition
import pywhatkit

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good morning,sir")
    elif(hour>12 and hour<=18):
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("Please tell me,How can i help u sir")

def curtime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak("time is {} sir".format(current_time))


