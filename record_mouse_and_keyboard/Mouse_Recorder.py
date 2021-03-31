from pynput import mouse
from pynput import keyboard
# Mouse
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    data_file = open("c:/Users/saket/Desktop/python files/record_mouse_and_keyboard/mouse_track.txt", 'a')
    # data = (str('{0} at {1}'.format('Pressed' 'Pressed' if pressed else 'Released', (x, y))))
    data = ('{0} {1};'.format(x, y))
    print(data)
    data_file.write(data)

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    if dy > 0:
        return False
# Keyboard
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False



# Collect events until released
def steps_record():
    # while True:
    with mouse.Listener and keyboard.Listener(
        # on_move=on_move,# NOTE remove the # to record the mouse move
        on_click=on_click,
        on_scroll=on_scroll,# as listener:
        # listener.join()ee
    # with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

steps_record()