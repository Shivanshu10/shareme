from shareme.client import Client
from shareme.server import Server
from shareme.cryp import Crypto
from shareme.cmpress import Compresser
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
        self.__cryp=Crypto(client_or_server=1)
        self.setUp()

    def setUp(self):
        pubk=self.__cryp.pubm
        if (self.__type):
            self.__sock.receiveBroadcast()
            otherk=self.receive(encr=False)
            self.__cryp.otherPub(otherk)
            print(self.__cryp.encodedPub())
            self.send(self.__cryp.encodedPub(), encr=False)

        else:
            thread_server=threading.Thread(target=self.__sock.threadedServer)
            thread_server.start()
            self.__sock.sendBroadcast()
            self.send(self.__cryp.encodedPub(), encr=False)
            otherk=self.receive(encr=False)
            self.__cryp.otherPub(otherk)

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

    def send(self, ch, encr=True):
        print("SENDING: " + str(ch))
        msg=Compresser.compress(ch)
        if (encr):
            msg=self.__cryp.encryptAsym(msg)
        self.__sock.send(msg)
        time.sleep(1)

    def receive(self, encr=True):
        msg=self.__sock.receive()
        if (encr):
             msg=self.__cryp.decryptAsym(msg)
        print(Compresser.decompress(msg))
        return Compresser.decompress(msg)