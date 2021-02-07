from os import walk

class Dir():
    def __init__(self, path):
        self.__path=path

    def walkDir(self):
        yield walk(self.__path, topdown=True)

    @property
    def get_path(self):
        return self._path