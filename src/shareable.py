from os.path import isdir, isfile
from dir import Dir
from file import File

class Shareable():
    def __init__(self, path):
        self.__path=path
        self.__is_dir=Shareable._isDir()
        if (self.__is_dir):
            self.__shareable_instanse=Dir(self.__path)
        else:
            self.__shareable_instanse=File(self.__path)
    
    @staticmethod
    def _isDir(path):
        return isdir(path)

    @staticmethod
    def _isFile(path):
        return isfile(path)
    
    def sendShareable():
        pass

    def receiveShareable():
        pass

    def sendMakeDir():
        pass

    def receiveMakeDir():
        pass