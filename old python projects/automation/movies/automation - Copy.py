# movie = input('Enter the movie name: ')
import webbrowser
webbrowser.open('https://moviesverse.in/')
import pyautogui as py
import time

def repeate(keyname, times):
    for i in range(times):
        py.hotkey(keyname)

sleep = time.sleep
locate = py.locateCenterOnScreen
sleep(2)
py.hotkey('shift', 'alt', 't')
repeate('tab', 3)
sleep(0.5)
py.typewrite('http://moviesverse.in/');py.hotkey('tab')
py.typewrite('endgame');py.hotkey('enter')
# py.hotkey('win', 'r'); py.typewrite('cmd')
# py.hotkey('enter');sleep(1)
# py.typewrite("Hey, You have to CLICK ON THE MOVIE can't identify it. ", interval=0.1)endgame
