import speech_recognition as sr
import pyttsx3
import time
r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

pyttsx3.speak(
    "this is a form to get informations about your name and age ")
time.sleep(1)

with sr.Microphone() as source:
    try:
        pyttsx3.speak("what's your name")
        message = r.record(source, duration=3)
        Name = r.recognize(message)
        print(Name)
    except:
        Name = "Aanandhene"
        print("ERROR")

with sr.Microphone() as source:
    try:
        pyttsx3.speak("whats your age")
        message2 = r1.record(source, duration=3)
        Age = r1.recognize(message2)
        print(Age)
    except:
        print("ERROR")
        Age = "18"  # default

with sr.Microphone() as source:
    try:
        pyttsx3.speak("whats your gender")
        message3 = r2.record(source, duration=3)
        Gender = r2.recognize(message3)
        print(Gender)
    except:
        Gender = "female"  # default
        print("ERROR")
