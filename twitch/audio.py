import speech_recognition

class audioRecognition:
    currentMsg:str
    recognizer: speech_recognition.Recognizer

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.currentMsg = ""

    def listen(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio) 
                self.currentMsg = text.lower() #converts upper to lower
                return self.currentMsg
        
        except Exception as e:
            self.recognizer = speech_recognition.Recognizer() #try again
        


