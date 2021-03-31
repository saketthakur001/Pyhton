import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser as wb
import os
import random
import difflib

query = "play magenta"

music_dir = "music"
songs_lst = os.listdir(music_dir)
print(songs_lst)



if 'play' in query: # Play a particular music
    qry = query.split()
    song_loc = qry.index("play") + 1
    song = qry[song_loc]
    print(song)
    songname = difflib.get_close_matches("Attention.mp3", songs_lst)
    print(songname)


    #os.startfile(os.path.join(music_dir, songs_lst[9]))