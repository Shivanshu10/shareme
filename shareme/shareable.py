import os
from shareme.dir import Dir
from shareme.file import File
from shareme.net import Net

class Shareable():
    def __init__(self, path, client_or_server):
        # 1 means client
        self.__path=path
        self.__root=path
        self.__client_or_server=client_or_server
        self.__net=Net(client_or_server)
        if (client_or_server==0):
            self.__root=os.path.join(self.__path, '..')
            self.__initSend()
        if (client_or_server):
            os.chdir(self.__root)
    
    def __initSend(self):
        self.__is_dir=Shareable._isDir(self.__path)
        if (self.__is_dir):
            self.__shareable=Dir(self.__path, self.__root)
        else:
            self.__shareable=File(self.__path, self.__root)
    
    @property
    def client_or_server(self):
        return self.__client_or_server

    @property
    def root_dir(self):
        return self.__root

    @staticmethod
    def _isDir(path):
        return os.path.isdir(path)

    @staticmethod
    def _isFile(path):
        return os.path.isfile(path)
    
    def send(self):
        self.__shareable.send(self.__net)
        self.__net.send(b"FINISH")
        self.__net.receive()

    def receive(self):
        while (True):
            received_data=self.__net.receive()
            if (received_data==b"FILE"):
                path=self.__net.receive().decode('utf-8')
                size=self.__net.receive().decode('utf-8')
                File.receive(self.__net, path)
            elif (received_data==b"DIR"):
                Dir.receive(self.__net)
            elif (received_data==b'FINISH'):
                self.__net.send(b"OK FINISH")
                break