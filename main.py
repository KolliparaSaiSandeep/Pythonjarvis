import os
import speedtest as speedtest
from bs4 import BeautifulSoup
import pyttsx3
import requests
import speech_recognition
import greetme
from datetime import datetime
import pyautogui
import cv2
import numpy as np


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

def alarm(query):
    timehere=open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")



if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        from greetme import greet
        greet()
        while True:
            query=takeCommand().lower()
            if "go to sleep" in query:
               speak("Ok sir,u can call anytime")
               break
            elif "current time" in query:
                greetme.curtime()
            elif "feeling alone" in query:
                speak("I am there for u sir ,dont worry")
            elif "thank u" in query:
                speak("u are welcome sir")
            elif "google" in query:
                from search import searchgoogle
                searchgoogle(query)
            elif "youtube" in query:
                from search import searchyoutube
                searchyoutube(query)
            elif "wikipedia" in query:
                from search import searchwikipedia
                searchwikipedia(query)
            elif "hello" in query:
                speak("Hello sir, how are you ?")
            elif "i am fine" in query:
                speak("that's great, sir")
            elif "how are you" in query:
                speak("Perfect, sir")

            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir, the time is {strTime}")

            elif "thank you" in query:
                speak("you are welcome, sir")
            elif "temperature" in query:
                search="temperature in Bangalore"
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeaWE").text
                speak(f"current {search} is {temp}")
            elif "sleep" in query:
                speak("Going to sleep,sir")
                exit()
            elif "open" in query:
                from Dictapp import openappweb
                openappweb(query)
            elif "close" in query:
                from Dictapp import closeappweb
                closeappweb(query)
            elif "pause" in query:
                pyautogui.press("k")
                speak("video paused")
            elif "play" in query:
                pyautogui.press("k")
                speak("video played")
            elif "mute" in query:
                pyautogui.press("m")
                speak("video muted")

            elif "volume up" in query:
                from keyboard import volumeup
                speak("Turning volume up,sir")
                volumeup()
            elif "volume down" in query:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()
            elif "screenshot" in query:
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image),
                                     cv2.COLOR_RGB2BGR)
                cv2.imwrite("image1.png", image)

            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "")
                rememberMessage = query.replace("jarvis", "")
                speak("You told me to remember that" + rememberMessage)
                remember = open("Remember.txt", "a")
                remember.write(rememberMessage)
                remember.close()
            elif "what do you remember" in query:
                remember = open("Remember.txt", "r")
                speak("You told me to remember that" + remember.read())
            elif "internet speed" in query:
                wifi = speedtest.Speedtest()
                upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                download_net = wifi.download() / 1048576
                print("Wifi Upload Speed is", upload_net)
                print("Wifi download speed is ", download_net)
                speak(f"Wifi download speed is {download_net}")
                speak(f"Wifi Upload speed is {upload_net}")
            elif "translate" in query:
                from Translator import translategl
                query = query.replace("jarvis", "")
                query = query.replace("translate", "")
                translategl(query)
            elif "rock paper scissors" in query:
                from game import game_play
                game_play()
            elif "whatsapp" in query:
                from whatsapp import sendMessage
                sendMessage()
            elif "shutdown the system" in query:
                speak("Are You sure you want to shutdown")
                shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
                elif shutdown == "no":
                    break






