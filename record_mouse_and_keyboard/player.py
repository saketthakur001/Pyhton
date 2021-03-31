import pyautogui
from time import sleep

file = open("c:/Users/saket/Desktop/python files/record_mouse_and_keyboard/mouse_track.txt", 'r')
lis = str(file.read()).split(';')




even = 0
for i in range(10):
    print(even)
    pos = lis[even].split(' ')
    x = int(pos[0])
    y = int(pos[1])
    print(x, y)
    sleep(0.5)
    pyautogui.click(x, y)
    even += 2