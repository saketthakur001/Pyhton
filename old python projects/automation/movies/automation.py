# print('The spelling should be correct')
# movie = input('Enter the movie name: ')
from webbrowser import open as web
# web('https://moviesverse.in/')
from pyautogui import locateCenterOnScreen, scroll, hotkey, typewrite, click
from time import sleep

# download_link = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\download link.png")
# download_anyway = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\download_anyway.png")
# direct_download = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\direct_download.png")
# fast_server = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\fast_server.png")
# generate_link = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\generate_link.png")
unlock_button = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\unlock.png")
# download_link_here = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\download_link_here.png")

# def repeate(keyname, times):
#     for i in range(times):
#         hotkey(keyname)

# hotkey('shift', 'alt', 't')
# repeate('tab', 3)
# sleep(0.6)
# typewrite('http://moviesverse.in/', interval = 0.05);hotkey('tab')
# sleep(0.5)
# typewrite('endgame', interval = 0.2);hotkey('enter')
# hotkey('win', 'r'); typewrite('cmd')
# hotkey('enter')
# sleep(1)
# hotkey('win', 'right')
# sleep(1)
# hotkey('alt','tab')
# sleep(1)
# hotkey('win', 'down')
# typewrite("You have 20 sec click on the movie and the download link", interval=0.1)
# sleep(20)
hotkey('alt', 'tab')
click(unlock_button);print(unlock_button)
# sleep(5)
# click(generate_link)
# sleep(2)
# click(download_link_here)
# sleep(2)
# click(fast_server)
# sleep(2)
# click(direct_download)
# sleep(1)
# click(download_anyway)