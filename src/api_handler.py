"""Module that is used to make calls and recieve from the API"""

from google.cloud import translate_v2


class Apihandler:
    """Class that represents the Api handling"""

    def __init__(self):
        Client = translate_v2.Client()
        Client.detect_language("shudsuhds")
