class File():
    def __init__(self, path):
        self.__path=path
        self.__f=None
    
    def openFile(self, op='rb'):
        self.__f=open(self.__path, op)
    
    def closeFile(self):
        self.__f.close()

    @property
    def file(self):
        return self.__f

    @property
    def get_path(self):
        return self.__path