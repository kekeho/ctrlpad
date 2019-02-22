import pyautogui
import json


class Key():
    def __init__(self, setting_json_filename):
        self.setting_json_filename = setting_json_filename
        with open(setting_json_filename) as pads_file:
            self.pads = json.load(pads_file)

    def update_setting(self):
        with open(self.setting_json_filename) as pads_file:
            self.pads = json.load(pads_file)

    def tap(self, pad_id):
        """When tapped pad, call this function.
        This function press hotkey.
        Arg:
            pad_id: pad's uuid
        """
        key = self.pads[pad_id]['hotkey']
        pyautogui.hotkey(*key)


# FOR DEBUG
if __name__ == "__main__":
    key = Key()
