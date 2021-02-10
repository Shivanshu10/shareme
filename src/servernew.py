import socket

class File():
    def __init__(self, path):
        self.__path = path
        self.__f = None

    def openFile(self, op='rb'):
        self.__f = open(self.__path, op)

    def closeFile(self):
        self.__f.close()

    def sersock(self):
        self.__f = socket.socket()
        print('Socket Created')

        self.__f.bind(('localhost', 9992))

        self.__f.listen(3)
        print('waiting for connection')

        while True:
            c, addr = s.accept()
            name = c.recv(4096).decode()
            print("Conneected with client", addr, name)
            with open (filename,"rb") as file:
                data=file.read(1024)
                while data:
                    c.send(data)
                    print(f"sent {data!r}")
                    data = file.reta(1024)
            print("file sent complete")
            c.close()



    @property
    def file(self):
        return self.__f

    @property
    def get_path(self):
        return self.__path