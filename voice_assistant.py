import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import time
import keyboard
engine = pyttsx3.init()
recognizer = sr.Recognizer()

pyautogui.FAILSAFE = False
def speak(text):

    print(f"\n🤖 {text}")

    engine.say(text)

    engine.runAndWait()