from pynput import keyboard
def on_press(key):
    print(key)

    
if __name__=="__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
        lsn.join()
