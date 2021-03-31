import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser as wb
import os
import random
import difflib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices)

music_dir = "C:\\Users\\saket\\Music"
songs_lst = os.listdir(music_dir)


def speak(audio):# Its a voice model
    engine.say(audio)
    engine.runAndWait()

def wishMe():# It Says every time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am noah, how can I help")

def takeCommand():# Recognizes
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
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for excuting tasks
        if "wikipedia" in query: # wifkipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query: # Youbube
            wb.open('youtube.com')
        
        elif "play music" in query: # random Music
            os.startfile(os.path.join(music_dir, songs_lst[random.randint(0, 100)]))
        
        elif 'clear temperary files' in query:
            pass
        elif "date" in query:
            speak("today is ", )
        elif "time" in query:
            now = datetime.datetime.now().strftime("it's %I:%M %p").lstrip("0")
            speak(now)

        elif "your name" in query:
            speak("already told you, it's, noah")

        elif "nice name" in query:
            speak("Thanks")
            speak("what is your name?")
            query = takeCommand().lower()
            speak("I will remember that")
        
        elif "how are you" in query:
            speak("I am good, what about you?")

        elif "fine" in query:
            speak("That makes us even")
        
        elif "you doing" in query:
            speak("thinking all the time how the universe works")

        elif "cool" in query:
            speak("But I am feeling Hot")

        elif "my name" in query:
            speak("Ok i will remember")