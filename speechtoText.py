import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
# sr.energy_threshold = 300
r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

time.sleep(1)
pyttsx3.speak(
    "male")

with sr.Microphone() as source:
    # try:
        pyttsx3.speak("what's your name")
        message = r.record(source, duration=2)
        Name = r.recognize(message)
        print(Name)
    # except :
        # Name = "Aanandhene"
        # print("ERROR")
