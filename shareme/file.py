import os
import shareme.consts

class File():
    def __init__(self, path, root):
        self.__path=path
        self.__root=root
        self.__size=os.path.getsize(self.__path)

    @staticmethod
    def openFile(path, op='rb'):
        f=open(path, op)
        return f

    @staticmethod
    def closeFile(f):
        f.close()

    @property
    def fname(self):
        return os.path.basename(self.__path)

    @property
    def fsize(self):
        return self.__size

    @property
    def path(self):
        return self.__path

    @staticmethod
    def __isEOF(f):
        cur = f.tell()    # save current position
        f.seek(0, os.SEEK_END)
        end = f.tell()    # find the size of file
        f.seek(cur, os.SEEK_SET)
        return cur == end

    def send(self, net):
        net.send(b"FILE")
        net.send(b"<SEPRATOR>")
        net.send(bytes(os.path.relpath(self.__path, start=self.__root), 'utf-8'))
        net.send(b"<SEPRATOR>")
        net.send(bytes(str(self.__size), 'utf-8'))
        net.send(b"<SEPRATOR>")
        file=File.openFile(self.__path)
        ch=[1, 2]
        while(len(ch)!=0):
            ch=file.read(shareme.consts.buffer)
            net.send(ch)
        net.send(b"END")
        net.send(b"<SEPRATOR>")
        File.closeFile(file)

    @staticmethod
    def receive(net, path):
        ch=net.receive()
        file=File.openFile(path, op='wb')
        while (ch!=b"END"):
            file.write(ch)
            ch=net.receive()
        File.closeFile(file)

    def __del__(self):
        del self.__path