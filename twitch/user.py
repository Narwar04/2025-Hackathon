import random
from server import ryansServer

messages_default = ["POG", "LMAO", "BAD", "L", "-2", "+2", "BOOOOOOOO"] 

class User:
    id: int               # id for user
    name: str             # name of user
    lmmessages: list[str] # list of generated lm messages
    messages: list[str]   # default messages

    def __init__(self, id, name, lmmessages): #initialization func
        self.id = id
        self.name = self.userColor(name)
        self.lmmessages = lmmessages
        self.messages = messages_default

    def userColor(self, name):
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])][0]
        return f'<span style="color:{color}">{name}</span>'

    def addMessage(self, message: str):
        self.messages.append(message)

    def sendDefaultMessage(self):
        msglen = len(self.messages) - 1
        msg = f'<br>{self.name}: {self.messages[random.randint(0, msglen)]}'
        return msg
    
    def sendLMMessage(self, prompt:str, server:ryansServer):
        server.sendPrompt(prompt)
        msg = server.recieveResonce()
        msg = f'<br>{self.name}: {msg}'
        return msg


    



# user1 = User(21, "user21", [], [])

# # print(user1.messages)
# user1.addMessage("Hello!!!!")
# # print(user1.messages)
# user1.displayMessage(message=(user1.messages[0]))

