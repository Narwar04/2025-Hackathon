#!/usr/bin/env python3

from time import sleep
import random
import threading

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
            
    def startChat(self, server: ryansServer):
        worker = threading.Thread(target=worker_thread, args=(self, server))
        worker.start()

        while True:
            user = self.users[(random.randint(0, self.usercnt) - 1)]
            self.guiObj.qtprint(user.sendDefaultMessage())
            sleep(random.random()/self.speed)

stop_event = threading.Event()

def worker_thread(chat: Chat, server: ryansServer):
    while True:
        if stop_event.is_set():
            break

        user = chat.users[(random.randint(0, chat.usercnt) - 1)]
        chat.guiObj.qtprint(user.sendLMMessage("""Generate a Twitch chat message, only the chat message.
                                 We will take your response directly and append it to a username.
                                 Feel free to add emojis. Make it incredibly brainrot. This format: message""", server))



