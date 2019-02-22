import pyautogui
import json
import uuid


class Key():
    def __init__(self, setting_json_filename):
        self.setting_json_filename = setting_json_filename
        with open(setting_json_filename) as pads_file:
            self.pads = json.load(pads_file)

    def update_setting(self):
        with open(self.setting_json_filename, 'w') as pads_file:
            json.dump(obj=self.pads, fp=pads_file)

    def tap(self, pad_id):
        """When tapped pad, call this function.
        This function press hotkey.
        Arg:
            pad_id: pad's uuid
        """
        key = self.pads[pad_id]['hotkey']
        pyautogui.hotkey(*key)

    def add_pad(self, name, *hot_key):
        """register pad to setting json file
        Args:
            name: pad's name
            *hot_key: when tap pads, press hotkeys
        """
        gen_uuid = str(uuid.uuid4())
        self.pads[gen_uuid] = {'name': name, 'hotkey': hot_key}
        self.update_setting()


# FOR DEBUG
if __name__ == "__main__":
    key = Key()
