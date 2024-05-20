import speech_recognition as sr
import datetime
import pyttsx3
import pywhatkit
import subprocess
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recogniser=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...")
        recogniser.adjust_for_ambient_noise(source,duration=0.5)
        print("Ask me anything")
        recordedaudio=recogniser.listen(source)
    try:
        user_input =recogniser.recognize_google(recordedaudio).lower()
        print('your message:',format(user_input))
    except Exception as ex:
        print(ex)

    if 'time' in user_input:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'search' in user_input:
        b='searching'
        engine.say(b)
        engine.runAndWait()
        query = user_input.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        print("searching for {query}")
while True:
    cmd()


