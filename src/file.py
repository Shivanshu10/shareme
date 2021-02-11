class File():
    def __init__(self, path):
        self.__path=path
        self.__f=None
    
    def _openFile(self, op='rb'):
        self.__f=open(self.__path, op)
        return self.__f
    
    def _closeFile(self):
        self.__f.close()

    @property
    def _file(self):
        return self.__f

    @property
    def path(self):
        return self.__path

    def send(self, net):
        file=self._openFile()
        while(file):
            ch=file.read()
            net.send(ch)
        
    def receive(self, ch):
        file=self._openFile(op='wb')
        file.write()

    def __del__(self):
        del self.__path
        del self.__f