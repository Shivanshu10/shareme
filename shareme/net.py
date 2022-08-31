from shareme.client import Client
from shareme.server import Server
from shareme.cryp import Crypto
from shareme.cmpress import Compresser
import threading

class Net():
    def __init__(self, client_or_server):
        # 1 means client
        self.__type=client_or_server
        if (client_or_server):
            self.__sock=Client()
        else:
            self.__sock=Server()
        self.__cryp=Crypto(self.__type)
        self.setUp()

    def setUp(self):
        if (self.__type):
            self.__sock.receiveBroadcast()
            otherk=self.receive(encr=False)
            self.__cryp.otherPub(otherk)
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
        print("MSG SEND: " + str(ch))
        msg=Compresser.compress(ch)
        print("COMPRESSED SEND: " + str(msg))
        if (encr):
            msg=self.__cryp.encryptAsym(msg)
            print("ENCRYPTED SEND: " + str(msg))
        print("SEND LEN")
        print(str(len(msg)).encode('utf-8'))
        self.__sock.send(str(len(msg)).encode('utf-8'))
        print("SEND MSG")
        self.__sock.send(msg)

    def receive(self, encr=True):
        print("RECV LEN")
        buffer=self.__sock.receive()
        print(buffer)
        buffer=int(buffer.decode('utf-8'))
        print(buffer)
        print("RECV MSG")
        msg=self.__sock.receive(buffer)
        print("ENCRYPTED RECV: " + str(msg))
        if (encr):
            msg=self.__cryp.decryptAsym(msg)
            print("COMPRESSED RECV: " + str(msg))
        msg=Compresser.decompress(msg)
        print("MSG RECV: " + str(msg))
        return msg