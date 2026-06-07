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
def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        try:

            audio = recognizer.listen(source, timeout=5)

            command = recognizer.recognize_google(audio).lower()

            print(f"✅ YOU SAID: {command}")

            return command

        except sr.UnknownValueError:

            print("❌ Could not understand")

            return ""

        except Exception as e:

            print("⚠️ ERROR:", e)

            return ""
