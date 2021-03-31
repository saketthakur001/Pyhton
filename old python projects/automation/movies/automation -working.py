# # movie = input('Enter the movie name: ')
# from webbrowser import open as web
# web('https://moviesverse.in/')
from pyautogui import locateCenterOnScreen, hotkey, typewrite, click
# from time import sleep
generate_link = locateCenterOnScreen("generate_link.png")
unlock_button = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\unlock.png")
download_link_here = locateCenterOnScreen("D:\\PYTHON\\1python_py_files\\1.PROJECTS\\automatioin\\movies\\download_link_here.png")
# def repeate(keyname, times):
#     for i in range(times):
#         py.hotkey(keyname)

# sleep = time.sleepc
# sleep(2)
# py.hotkey('shift', 'alt', 't')
# repeate('tab', 3)
# sleep(0.5)
# py.typewrite('http://moviesverse.in/');py.hotkey('tab')
# py.typewrite('endgame');py.hotkey('enter')
# py.hotkey('win', 'r'); py.typewrite('cmd')
# py.hotkey('enter');sleep(1)
# py.typewrite("Hey, You have to CLICK ON THE MOVIE can't identify it. ", interval=0.1)
# the choice
# py.click(unlock_button)
# sleep(3)
# py.click(generate_link)
# sleep(2)
# py.click(download_link_here)