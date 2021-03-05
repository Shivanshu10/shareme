from shareme.client import Client
from shareme.server import Server
from shareme.cryp import Crypto
from sharme.cmpress import Compresser
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
        pubk=self.__cryp.pubm()
        if (self.__type):
            self.__sock.receiveBroadcast()
            otherk=self.receive()
            self.__cryp.otherPub(otherk)
            self.send(pubk)
            key_encrypted=self.__cryp.encryptKey()
            self.send(key_encrypted)
        else:
            thread_server=threading.Thread(target=self.__sock.threadedServer)
            thread_server.start()
            self.__sock.sendBroadcast()
            self.send(pubk)
            otherk=self.receive()
            self.__cryp.otherPub(otherk)
            key_encrypted=self.__cryp.encryptKey()
            self.send(key_encrypted)
            key_encrypted=self.receive()
            self.__cryp.setKey(self.__cryp.decryptAsym(key_encrypted))

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
        msg=Compresser.compress(ch)
        msg=self.__cryp.encryptSym(msg)
        self.__sock.send(msg)
        time.sleep(1)

    def receive(self):
        msg=self.__cryp.decryptSym(self.__sock.receive())
        return Compresser.decompress(msg)