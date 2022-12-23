import os

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
