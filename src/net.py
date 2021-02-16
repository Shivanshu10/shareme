from client import Client
from server import Server

class Net():
    def __init__(self, client_or_server):
        # 1 means client
        self.__type=client_or_server
        if (client_or_server):
            self.__sock=Client()
        else:
            self.__sock=Server()

    def setUp(self):
        if (self.__type):
            self.__sock.receiveBroadcast()
        else:
            self.__sock.sendBroadcast()

    @property
    def timeout(self):
        return self.__sock.timeout

    @property
    def ip_bind(self):
        return self.__sock.ip_bind

    @property
    def port_bind(self):
        return self.__sock.port_bind

    @property
    def ip(self):
        return self.__sock.ip

    @property
    def sock(self):
        return self.__sock.sock

    def send(self, ch):
        self.__sock.send(ch)

    def receive(self):
        return self.__sock.receive()