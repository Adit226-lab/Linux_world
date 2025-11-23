import matplotlib.pyplot as plt
import pyttsx3
import os
import webbrowser
import speech_recognition as sr
import pywhatkit

speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Welcome to Bixby")
speaker.runAndWait()

with sr.Microphone() as source:
    print("Start speaking...")
    mic.adjust_for_ambient_noise(source, duration=1)

    try:
        voice = mic.listen(source, timeout=5, phrase_time_limit=5)
        text = mic.recognize_google(voice)
        command = text.lower()
        print("You said:", command)

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        command = ""

    except sr.RequestError:
        print("Speech service down.")
        command = ""

    except sr.WaitTimeoutError:
        print("No speech detected.")
        command = ""

# ---------------- COMMANDS ----------------

if "open notepad" in command:
    print("Opening Notepad...")
    os.system("notepad")

elif "open youtube" in command:
    print("Opening YouTube...")
    webbrowser.open("https://youtube.com")

elif "open whatsapp" in command or "send message" in command:
    print("Sending WhatsApp message...")

    try:
        pywhatkit.sendwhatmsg_instantly("+919548892134", "hi i am from vgu", wait_time=10, tab_close=True)
        print("Message sent!")

    except Exception as e:
        print("Error while sending message:", e)

elif command != "":
    print("Command not recognized.")

