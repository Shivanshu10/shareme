import os
from shareme.file import File
import time

class Dir():
    def __init__(self, path, root):
        self.__path=path
        self.__root=root
        self.__size=os.path.getsize(self.__path)

    def walkDir(self):
        return os.walk(self.__path, topdown=True)

    def send(self, net, is_root=True):
        net.send(b"DIR")
        net.send(bytes(os.path.relpath(self.__path, start=self.__root), 'utf-8'))
        net.send(bytes(str(self.__size), 'utf-8'))
        net.send(b"END")
        time.sleep(2)
        if (is_root):
            for root, dirs, files in self.walkDir():
                for name in files:
                    print(root)
                    File(os.path.join(root, name), self.__root).send(net)
                    time.sleep(2)
                for name in dirs:
                    Dir(os.path.join(root, name), self.__root).send(net, is_root=False)

    @staticmethod
    def receive(net):
        path=net.receive().decode('utf-8')
        print("PATH: " + path)
        size=net.receive().decode('utf-8')
        print("SIZE: " + size)
        Dir._makeDir(path)
        net.receive()

    @property
    def path(self):
        return self.__path
    
    @property
    def fname(self):
        return os.path.basename(self.__path)

    @property
    def fsize(self):
        return self.__size

    @staticmethod
    def _makeDir(path):
        os.mkdir(path)

    def __del__(self):
        del self.__path