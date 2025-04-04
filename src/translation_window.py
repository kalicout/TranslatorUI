"""Module that is used to generate/control the GUI"""

import tkinter as tk


class TranslatorWindow:
    """Class that represents the Pop up window"""

    def __init__(self, pointerpos, text, wid):
        self.position = pointerpos
        self.text = text
        self.window_id = wid
        self.window = None
        self.create_window()

    def create_window(self):
        """Creates the actual tkinter window"""
        self.window = tk.Tk()
        wd = self.window.winfo_screenwidth()
        he = self.window.winfo_screenheight()

        x = (wd / 2) - (self.position[0] / 2)
        y = (he / 2) - (self.position[1] / 2)

        self.window.geometry("%dx%d+%d+%d" % (wd, he, x, y))

        untranslated_text = self.text["input"]
        translated_text = self.text["translatedText"]
        text = tk.Label(
            text=untranslated_text + " \n" + translated_text, font=("Helvetica", 20)
        )
        text.pack()
        self.window.mainloop()
