from chat import *

if __name__ == '__main__':
    stop_event = threading.Event()
    signal.signal(signal.SIGINT, handle_kb_interrupt)
    server = ryansServer(sock=None) #init serer
    chat = Chat(5, 0.5, server) #init chat
    chat.startChat(server=server)
