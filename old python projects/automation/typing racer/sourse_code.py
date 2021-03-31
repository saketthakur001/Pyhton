import pyautogui as py
import pyscreeze

move = py.moveTo
hk = py.hotkey
ty = py.typewrite
cl = py.click

scrshot = py.screenshot
pause = py.PAUSE

hk("win", "i"); ty(["ctrl"])
ty("location"); ty(['enter'])
privacy = locate("D:\\PYTHON\\1python_py_files\\bug fixer\\privacy_icon.png")
move(privacy); cl(duration = 0.1)

