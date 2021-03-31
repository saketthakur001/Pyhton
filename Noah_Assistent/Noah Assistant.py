import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
from time import sleep
import webbrowser as wb
import os
import subprocess
import random
import difflib
import pyautogui
import getpass

username = getpass.getuser()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices)
name_lst = []
music_dir = "C:/Users/" + username + "/Music"# add a music folder location
songs_lst = os.listdir(music_dir)


def speak(audio): # Its a voice model
    engine.say(audio)
    engine.runAndWait()


def takeCommand(): # Recognizes
    # it takes imcrophone input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: ", query)

    except Exception:
        # [print(e)]
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower() # Logic for excuting tasks

        if "wikipedia" in query: # wifkipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open chrome' in query: # Youbube

            speak("opening chrome")
        
        elif "play music" in query: # random Music
            os.startfile(os.path.join(music_dir, songs_lst[random.randint(0, 100)]))
        
        elif 'temporary' in query: # this will clear your temperary files
            subprocess.call("del /q/f/s %TEMP%\*", shell=True)
            speak("temporary files deleted")
            print("temporary files deleted")

        elif "date" in query: # If you ask him the date
            speak("today is ", )

        elif "time" in query:# If you ask him the time
            now = datetime.datetime.now().strftime("it's %I:%M %p").lstrip("0")
            speak(now)

#-----------------------------------------------------------------------------------------------------------------------------------------

        elif "your name" in query:# If you ask his name
            speak("already told you, it's, noah")

        elif "nice name" in query:# If you tell him he has a nice name
            speak("Thanks")
            speak("what is your name?")
            query = takeCommand().lower()
            speak("I will remember that")
        
        elif "how are you" in query:# If you ask him "how are you"
            speak("I am good, what about you?")

        elif "fine" in query:# If you say you are fine
            speak("That makes us even")
        
        elif "you doing" in query:# If you ask him what he is doing
            speak("thinking all the time how the universe works")

        elif "cool" in query: # If you use cool word
            speak("But I am feeling Hot")

        elif "my name" in query:# if you tell him your name
            speak("Ok, i will remember that")
            break
        elif "you think" in query:
            speak("yes, I do")
sleep(10)
print('10 sec passed')
sleep(10)