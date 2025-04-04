"""Module that is used to make calls and recieve from the API"""

from google.cloud import translate_v2


class Apihandler:
    """Class that represents the Api handling"""

    def __init__(self):
        self.client = translate_v2.Client()
        self.curr_language = None  # Current detected Language
        self.translation = None  # Current translation

    def translate_text(self, text):
        """Makes the call for the translation"""
        self.curr_language = self.client.detect_language(text)
        print("TEXT: ", text)
        print("CURL ", self.curr_language)

        if self.curr_language != "en":
            self.translation = self.client.translate(
                text,
                source_language=self.curr_language["language"],
                target_language="en",
            )
            print("TRANSLATION: ", self.translation)
            return self.translation

    def give_examples(self, text):
        """generates a bunch of examples for a given word"""
