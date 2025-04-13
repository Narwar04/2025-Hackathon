import socket
MAXLENG = 1024

class ryansServer:

    sock: socket
    host: str = "vpn.densmo.re"
    port: int = 6969
    def __init__(self, sock=None):
        if sock is None:
            print("hi:", self.host, self.port, "\n")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("set socket")
        else:
            self.sock = sock

    # connect to host    
    def connectServer(self):
        print("trying to connect")
        self.sock.connect((self.host, self.port))
        print("connected")

    def sendPrompt(self, prompt: str):
        self.sock.send(prompt.encode("utf-8")[:MAXLENG])
    
    def recieveResonce(self):
        responce = self.sock.recv(MAXLENG)
        responce = responce.decode("utf-8")
        return responce
    
    def close(self):
        self.sock.close()


# ryansServer1 = ryansServer(sock=None)

# ryansServer1.connectServer()

# while True:
#     ryansServer1.sendPrompt("Hello There")

#     str = ryansServer1.recieveResonce()

#     print(str)

# ryansServer1.close()
