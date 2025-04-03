"""Translator app"""

import keyboard
import pyperclip
import time
from src.translator import TranslatorUI


def copy_to_clipboard_and_read():
    """Copies highlighted text to clipboard and reads it"""
    keyboard.press("ctrl+c")
    keyboard.release("ctrl+c")
    return pyperclip.paste()


if __name__ == "__main__":
    Translator = TranslatorUI()

    hotkeys = ["up", "up", "up"]

    while True:
        key = keyboard.read_event()
        if key.name == "ctrl":
            hotkeys[0] = key.event_type
            print(hotkeys)

        if key.name == "alt gr":
            hotkeys[1] = key.event_type
            print(hotkeys)

        if key.name == "u":
            hotkeys[2] = key.event_type
            print(hotkeys)

        if "up" not in hotkeys:
            hotkeys = ["up", "up", "up"]
            time.sleep(0.1)
            clipText = copy_to_clipboard_and_read()
            print("Copied Text", clipText)
