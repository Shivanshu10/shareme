import os
from shareme.file import File

class Dir():
    def __init__(self, path, root):
        self.__path=path
        self.__root=root
        self.__size=os.path.getsize(self.__path)

    def walkDir(self):
        yield os.walk(self.__path, topdown=True)

    def send(self, net, is_root=True):
        net.send(b"DIR")
        net.send(bytes(os.path.relpath(self.__path, start=self.__root), 'utf-8'))
        net.send(bytes(str(self.__size), 'utf-8'))
        net.send(b"END")
        if (is_root):
            for root, dirs, files in self.walkDir():
                for name in files:
                    File(os.path.join(root, name), self.__root).send()
                for name in dirs:
                    Dir(os.path.join(root, name), self.__root).send(net, is_root=False)

    @staticmethod
    def receive(path):
        Dir._makeDir(path)

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