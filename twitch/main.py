#!/usr/bin/env python3

import threading
import sys

from server import ryansServer
from chat import Chat
from gui import Gui

chatObj = None

serverObj = None

def chatThread(guiObj):
    chatObj = Chat(5, 0.5, server, guiObj)
    chatObj.startChat(server)
    

server = ryansServer(sock=None) #init serer
guiObj = Gui()

thread = threading.Thread(target=chatThread, args=(guiObj,))
thread.start()

sys.exit(guiObj.app.exec())
