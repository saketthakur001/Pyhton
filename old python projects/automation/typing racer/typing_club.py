import pyautogui as py, time

sleep = time.sleep
hk = py.hotkey
tw = py.typewrite
ty = py.typewrite
click = py.click
move = py.moveTo
locate = py.locateCenterOnScreen



hk("win", "7" )
time.sleep(1)
click(386, 61)
hk("ctrl", "a")
ty("https://play.typeracer.com/")
sleep(0.1)
ty(["enter"])
sleep(1)
hk("ctrl", "shift", "i")
sleep(6)
click(594, 183)
sleep(0.5)
click(371, 261)
sleep(4)
click(850, 155)
time.sleep(1)
hk("ctrl", "a"); ty("nhwMiddlegwt")

time.sleep(1)
time.sleep(0.5)
tw(["enter"])
time.sleep(1)
tw(["enter"])
time.sleep(1)
py.doubleClick(1201, 442)#-----------------------------------name it
time.sleep(0.5)
hk("ctrl", "c")
time.sleep(0.5)
sleep(1)
py.moveRel(20, 40)
py.scroll(5000)#scroll
hk("win", "6")
time.sleep(1)
hk("ctrl", "pageup")
time.sleep
pageup = 0
time.sleep(0.5)
click(532, 333)#-------------------------------------------name it
hk("ctrl", "z"); hk("ctrl","z")
time.sleep(0.5)
hk("ctrl", "v")# This is working 😁😁
time.sleep(0.5)


hk("win", "7" )
time.sleep(1)
click(850, 155)
time.sleep(1)
hk("ctrl", "a"); ty("hwRightgwt")#-------2nd--ID--------####
time.sleep(1)
tw(["enter"])
time.sleep(1)# working-----------------------------------------------------------------------------------------

click(1033, 397)
time.sleep(1)
py.doubleClick(1070, 419)
time.sleep(0.5)
hk("ctrl", "c")
sleep(0.5)d
hk("ctrl", "shift", "i")
sleep(0.5)
hk("win", "7")
time.sleep(0.1)
hk("ctrl", "v")
click(1291, 38)

