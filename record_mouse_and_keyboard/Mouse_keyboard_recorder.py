import mouse
import keyboard

data = open(r"c:/Users/saket/Desktop/python files/record_mouse_and_keyboard/data.py")
# eve = []
# mouse.hook(eve.append)
# keyboard.wait("a")
# mouse.unhook(eve.append)
# print(eve)
# mouse.play(events, aspeed_factor=1.0, include_clicks=True, include_moves=True, include_wheel=True)


events = []                 #This is the list where all the events will be stored
mouse.hook(events.append)   #starting the mouse recording
keyboard.wait("a")          #Waiting for 'a' to be pressed
mouse.unhook(events.append) #Stopping the mouse recording
# mouse.play(events)          #Playing the recorded events

# data.write(str(events))
print(events)