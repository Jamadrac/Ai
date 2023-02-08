import sys
import threading
import tkinker as tk

import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant

class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker =tts.init()
        self.speaker.setProperty("rate",150)

        self.assistant = GenericAssitantant("intents.json", intent_methods={"file":self.create_file})
        self.assistant.train_model()

        self.root = tk.Tk()
        self.lable = tk.lable(text="")
    # if the response is not found 
    def create_file(self):
        pass
    