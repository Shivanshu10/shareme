import shareme.consts
import socket

class Server():
    def __init__(self):
        self.__client=None

    def __createSocketTCP(self):
        self.__s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __createSocketUDP(self):
        self.__broad=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    def __setOpts(self):
        self.__broad.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    def _bind(self, ip, port):
        self.__ip_bind=ip
        self.__port_bind=port
        self.__s.bind((ip, port))

    @property
    def ip_bind(self):
        return self.__ip_bind

    @property
    def port_bind(self):
        return self.__port_bind

    @property
    def ip(self):
        return self.__s.gethostbyname(self.__s.gethostname())

    @property
    def sock(self):
        return self.__s

    def receive(self, buffer=shareme.consts.buffer):
        self.__client.sendall(b"DONE PROCESSING")
        s=self.__client.recv(buffer)
        return s

    def send(self, ch):
        self.__client.recv(shareme.consts.buffer)
        self.__client.sendall(ch)

    def close(self):
        if (self.__client):
            self.__closeServer()
        self.__s.close()
    
    def _closeUDP(self):
        self.__broad.close()

    def __closeServer(self):
        self.__client.close()
    
    def threadedServer(self):
        self.__createSocketTCP()
        self._bind(shareme.consts.all_ip, shareme.consts.service_port)
        self.__s.listen(1)
        conn, addr=self.__s.accept()
        self.__client=conn
        self.__ip_bind=addr[0]
        self.__port_bind=addr[1]

    def sendBroadcast(self):
        self.__createSocketUDP()
        self.__setOpts()
        while (True):
            self.__broad.sendto(b"Hello lets share!!", ('<broadcast>', shareme.consts.broad_port))
            if (self.__client):
                break
        self._closeUDP()
        del self.__broad
        