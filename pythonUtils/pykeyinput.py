from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key %s pressed' % key.char)
    except AttributeError:
        print('special key %s pressed' % key)

def on_release(key):
    print('%s on release' % key)

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
