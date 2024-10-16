from pynput import keyboard


class FootSwitchListener:
    def __init__(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()  # start to listen on a separate thread
        listener.join()

    def on_press(self, key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        if k in ['!']:  # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            print('Key pressed: ' + k)
