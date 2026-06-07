# Import required libraries
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import time
import keyboard
# Initialize voice assistant
engine = pyttsx3.init()
recognizer = sr.Recognizer()
pyautogui.FAILSAFE = False
# Speak function
def speak(text):
    print(f"\n🤖 {text}")
    engine.say(text)
    engine.runAndWait()
# Listen function
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
# App launcher function
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
# Google search function
def search_google(command):
    search_term = command.replace("search", "")
    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.open(url)
    speak(f"Searching {search_term}")
# Typing function
def type_text(command):
    text = command.replace("type", "")
    pyautogui.write(text, interval=0.05)
    speak("Typing completed")
# Mouse control function
def mouse_control(command):
    if "move right" in command:
        pyautogui.moveRel(100, 0)
    elif "move left" in command:
        pyautogui.moveRel(-100, 0)
    elif "move up" in command:
        pyautogui.moveRel(0, -100)
    elif "move down" in command:
        pyautogui.moveRel(0, 100)
    elif "click" in command:
        pyautogui.click()
        speak("Mouse clicked")
    elif "double click" in command:
        pyautogui.doubleClick()
        speak("Double clicked")
    elif "right click" in command:
        pyautogui.rightClick()
        speak("Right click")
# Scrolling function
def scroll_control(command):
    if "scroll up" in command:
        pyautogui.scroll(500)
    elif "scroll down" in command:
        pyautogui.scroll(-500)
# Screenshot function
def take_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    speak("Screenshot taken")
# Volume control function
def volume_control(command):
    if "volume up" in command:
        for _ in range(5):
            keyboard.press_and_release("volume up")
    elif "volume down" in command:
        for _ in range(5):
            keyboard.press_and_release("volume down")
    elif "mute" in command:
        keyboard.press_and_release("volume mute")
# Window control function
def window_control(command):
    if "close window" in command:
        pyautogui.hotkey("alt", "f4")
        speak("Closing window")
    elif "minimize" in command:
        pyautogui.hotkey("win", "down")
    elif "copy" in command:
        pyautogui.hotkey("ctrl", "c")
    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")
# Display available commands
print("=" * 60)
print("🤖 VOICE CONTROLLED EVERYTHING")
print("=" * 60)
speak("Voice assistant started")
# Main program loop
while True:
    command = listen()
    if not command:
        continue
    if "open" in command:
        open_app(command)
    elif "search" in command:
        search_google(command)
    elif "type" in command:
        type_text(command)
    elif "move" in command or "click" in command:
        mouse_control(command)
    elif "scroll" in command:
        scroll_control(command)
    elif "screenshot" in command:
        take_screenshot()
    elif "volume" in command or "mute" in command:
        volume_control(command)
    elif (
        "close" in command
        or "copy" in command
        or "paste" in command
        or "minimize" in command
    ):
        window_control(command)
# Exit command
    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        break