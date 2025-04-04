"""Translator app"""

import os
import time
import keyboard
import pyperclip
from src.translator import TranslatorUI


def copy_to_clipboard_and_read():
    """Copies highlighted text to clipboard and reads it"""
    keyboard.press("ctrl+c")
    keyboard.release("ctrl+c")
    return pyperclip.paste()


if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        "/home/sapatri/.config/gcloud/application_default_credentials.json"
    )
    Translator = TranslatorUI()
    while True:  # Check if hotkey is pressed loop
        if keyboard.is_pressed("ctrl+altgr+u"):
            time.sleep(1)
            clipText = copy_to_clipboard_and_read()

            Translator.api_handler.translate_text(clipText)  # Actual translation Part
