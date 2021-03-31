import pyautogui as py, time

hk = py.hotkey
tw = py.typewrite
ty = py.typewrite
click = py.click
move = py.moveTo
locate = py.locateCenterOnScreen

hk("win", "7" )
time.sleep(1)
click(850, 155)
time.sleep(1)
hk("ctrl", "a"); ty("nhwMiddlegwt-uid-6")
move(1133, 417)
py.scroll(5000)# scroll---------
time.sleep(1)
time.sleep(0.5)
tw(["enter"])
time.sleep(1)
py.doubleClick(1133, 417)
time.sleep(0.5)
hk("ctrl", "c")
time.sleep(0.5)
hk("win", "6")
time.sleep(2)
hk("ctrl", "v")# This is working 😁😁

hk("win", "7" )
time.sleep(1)
py.scroll(5000)# scroll---------
time.sleep(1)
click(850, 155)
time.sleep(1)
hk("ctrl", "a"); ty("hwRightgwt")
time.sleep(0.5)
tw(["enter"])
time.sleep(1)# working-----------------------------------------------------------------------------------------

click(1028, 397)
time.sleep(1)
py.doubleClick(1070, 419)
time.sleep(0.5)
hk("ctrl", "c")
hk("win", "7")
time.sleep(1)
hk("trl", "pageup")
hk("ctrl", "v")
