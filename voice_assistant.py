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
def open_app(command):

    if "chrome" in command:

        os.system("start chrome")

        speak("Opening Chrome")

    elif "calculator" in command:

        os.system("calc")

        speak("Opening Calculator")

    elif "notepad" in command:

        os.system("notepad")

        speak("Opening Notepad")

    elif "paint" in command:

        os.system("mspaint")

        speak("Opening Paint")

    elif "youtube" in command:

        webbrowser.open("https://youtube.com")

        speak("Opening YouTube")

    elif "google" in command:

        webbrowser.open("https://google.com")

        speak("Opening Google")
def search_google(command):

    search_term = command.replace("search", "")

    url = f"https://www.google.com/search?q={search_term}"

    webbrowser.open(url)

    speak(f"Searching {search_term}")
