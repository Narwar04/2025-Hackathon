#!/usr/bin/env python3

from time import sleep
import random
import threading
from audio import audioRecognition
from user import User
from server import ryansServer
import gui

class Chat: 
    users: list[User] #list of users
    speed: float
    usercnt: int
    generatingMessage: bool    
    
    def __init__(self, usercnt:int, chatspd: float, server: ryansServer, guiObj: gui.Gui):
        self.users = []
        self.speed = chatspd
        self.usercnt = usercnt
        self.generatingMessage = False
        self.guiObj = guiObj

        server.connectServer()

        for i in range(usercnt):
            server.sendPrompt("""You are generating twitch chat names.
                               Please generate a random twitch chat name.
                              Just the name, nothing else. We will take this directly and append it to a message.
                              """)
            name = server.recieveResonce()
            self.users.append(User(i, name, []))
            
    def startChat(self, server: ryansServer, speechRecog: audioRecognition):
        global voiceMsg
        voiceMsg = ""
        worker = threading.Thread(target=worker_thread, args=(self, server,)) # sends stream of messages
        worker2 = threading.Thread(target=worker_thread2, args=(self, server, speechRecog,)) #takes care of speech
        # donationWorker = threading.Thread(target=donationMessage, args=(self,))
        worker.start()
        worker2.start()
        # donationWorker.start()
        worker

        while True:
            user = self.users[(random.randint(0, self.usercnt) - 1)]
            self.guiObj.qtprint(user.sendDefaultMessage())

            sleep(random.random()/self.speed)

def worker_thread(chat: Chat, server: ryansServer):
    global voiceMsg #globally modifys val
    while True:       
        user = chat.users[(random.randint(0, chat.usercnt) - 1)]

        chat.guiObj.qtprint(user.sendLMMessage("""Generate a Twitch chat message, only the chat message.
                                 We will take your response directly and append it to a username. Please
                                 respond to this message and make it pertain to what I say only
                                 What the streamer is saying: """ + voiceMsg, server))

def worker_thread2(chat: Chat, server: ryansServer, speechRecog: audioRecognition):
    global voiceMsg # globally modify this value
    while True:       
        speechRecog.listen()
        user = chat.users[(random.randint(0, chat.usercnt) - 1)]

        voiceMsg = speechRecog.currentMsg
        print("Recognized Speech:" + speechRecog.currentMsg)

        chat.guiObj.qtprint(user.sendLMMessage("""Generate a Twitch chat message, only the chat message.
                                 We will take your response directly and append it to a username. Please
                                 respond to this message and make it pertain to what I say only
                                 What the streamer is saying: """ + voiceMsg, server))

# def donationMessage(chat: Chat):
#     global voiceMsg # globally modify this value
#     while True:       
#         # user = chat.users[(random.randint(0, chat.usercnt) - 1)]
#         # if(random.random() < 0.10):
#         #         print("hello gui time")
#         #         # chat.guiObj.donationAlert(user.name)
