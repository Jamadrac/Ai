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

        self.assistant = GenericAssistant("intents.json", intent_methods={"file":self.create_file})
        self.assistant.train_model()

        # graphic user inter fa
        self.root = tk.Tk()
        self.lable = tk.Label(text="😼", font=("Arial", 120, "bold"))
        self.lable.pack()

        threading.Thread(target=self.run_assitant).start()
        self.root.mainloop()

    # if the response is not found 
    def create_file(self):
        pass

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.20)
                    audio =self.recognizer.listen(mic)
                    text = text.lower()

                    if "hey jake" in text:
                        self.lable.config(fg="red")
                        text = self.recognizer.recognize_google(audio)
                        text = text.lowers()
                        if text == "stop":
                            self.speaker.say("bye")
                            self.speaker.runAndWait()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response =self.assistant.request.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                                self.lable.config(fg="black")
            except:
                self.lable.config(fg="black")
                continue
    