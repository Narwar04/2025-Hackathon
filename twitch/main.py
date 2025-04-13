#!/usr/bin/env python

import threading
import sys

from server import ryansServer
from chat import Chat
from gui import Gui
from audio import audioRecognition



chatObj = None
serverObj = None

def chatThread(guiObj):
    audioRecog = audioRecognition()
    chatObj = Chat(5, 0.1, server, guiObj)
    chatObj.startChat(server, audioRecog) # for generating messages and for audio 
    

server = ryansServer(sock=None) #init serer
guiObj = Gui()

thread = threading.Thread(target=chatThread, args=(guiObj,))
thread.start()

sys.exit(guiObj.app.exec())
