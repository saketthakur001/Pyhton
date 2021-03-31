import pyautogui as py

live_loca = py.displayMousePosition
move = py.moveTo
hk = py.hotkey
ty = py.typewrite
cl = py.click
locate = py.locateCenterOnScreen
scrshot = py.screenshot
pause = py.PAUSE

hk("win", "r")
run = locate("D:\\PYTHON\\1python_py_files\\bug fixer\\run.png")
ty("mspaint")
ty(["enter"])
paint = locate("D:\\PYTHON\\1python_py_files\\bug fixer\\mspaint.png")
hk("win", "up")
blank = locate("D:\\PYTHON\\1python_py_files\\bug fixer\\blank.png")
move(blank)

