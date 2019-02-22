import pyautogui


class Key():
    def __init__(self, *args, **kwargs):
        pass

    def hotkey(self, *keys):
        """type keys at same time
        Arg:
            *keys: hotkeys
                example: ('ctrl', 'c')
        """
        pyautogui.hotkey(*keys)


# FOR DEBUG
if __name__ == "__main__":
    key = Key()
    key.hotkey('command', 'space')  # launch spotlight
