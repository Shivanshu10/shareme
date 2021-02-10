class Client():
    def __init__(self, path):
        self.__path = path
        self.__f = None

    def sercsock(self):
        self.__f = socket.socket()
        c.connect(('localhost', 9992))
        name = ("hi from client")
        c.send(bytes(name, 'utf-8'))
        with open("readfile.txt","wb") as file:
            print("File open")
            print("receiving data")
            while True:
                data = sock.rec(1024)
                print(f"data={data}")
                if not data:
                    break:
                file.write(data)
    print("Got the file")
    self.__f.close()
