"""Main program that manages everything"""

from . import api_handler
from . import translation_window


class TranslatorUI:
    """Create a daemon to run the program on the background and without stoping"""

    def __init__(self):
        self.api_handler = api_handler.Apihandler()
        self.translation_windows = {}
        self.window_count = 0

    def generate_window(self, pointerpos, text):
        """Generates a new window for a specific translation"""
        self.translation_windows[self.window_count] = (
            translation_window.TranslatorWindow(
                pointerpos=pointerpos, text=text, wid=self.window_count
            )
        )
        self.window_count += 1

    def remove_window(self):
        """Removes window"""

        # self.startDaemon()

    # def startDaemon(self):ç

    #     pass
