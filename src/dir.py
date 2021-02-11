from os import walk

class Dir():
    def __init__(self, path):
        self.__path=path

    def walkDir(self):
        yield walk(self.__path, topdown=True)

    def send():
        pass

    def receive():
        pass

    @property
    def path(self):
        return self._path
    
    def _makeDir(self):
        pass

    def __del__(self):
        del self.__path