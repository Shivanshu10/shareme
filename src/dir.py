import os

class Dir():
    def __init__(self, path):
        self.__path=path
        self.__dname=os.path.splitext(self.__path)

    def walkDir(self):
        yield os.walk(self.__path, topdown=True)

    def send(self):
        return self.__dname

    def receive(self):
        self._makeDir(self)

    @property
    def path(self):
        return self._path
    
    @property
    def fname(self):
        return self.__dname

    def _makeDir(self):
        path=os.path.join(self.path, self.__dname)
        os.mkdir(path)

    def __del__(self):
        del self.__path