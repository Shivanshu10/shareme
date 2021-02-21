from shareme.client import Client
from shareme.server import Server
import threading
import time


class Net():
    def __init__(self, client_or_server):
        # 1 means client
        self.__type=client_or_server
        if (client_or_server):
            self.__sock=Client()
        else:
            self.__sock=Server()
        self.setUp()

    def setUp(self):
        if (self.__type):
            self.__sock.receiveBroadcast()
        else:
            thread_server=threading.Thread(target=self.__sock.threadedServer)
            thread_server.start()
            self.__sock.sendBroadcast()

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
        print("SENDING: " + str(ch))
        self.__sock.send(ch)
        time.sleep(1)

    def receive(self):
        return self.__sock.receive()