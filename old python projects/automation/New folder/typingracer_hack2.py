import pyautogui as py, time
hk = py.hotkey
tw = py.typewrite
ty = py.typewrite
click = py.click
move = py.moveTo
locate = py.locateCenterOnScreen
sleep = time.sleep

hk("win", "7")
time.sleep(2)
loc = locate("D:\\PYTHON\\1python_py_files\\automatioin\\blank.png")
sleep(3)
click(loc)
sleep(0.5)
data = tw("  ", interval= 0.08)
sleep(2)
hk("win", "6")
sleep(1)
hk("ctrl", "pageup")
sleep(1) 
click(1291, 38)