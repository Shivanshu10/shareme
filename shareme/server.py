import shareme.consts
import socket
import time

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

    def receive(self):
        return self.__client.recv(shareme.consts.buffer)

    def send(self, ch):
        self.receive()
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

    def sendBroadcast(self, sleep_time=2):
        self.__createSocketUDP()
        self.__setOpts()
        while (True):
            self.__broad.sendto(b"Hello lets share!!", ('<broadcast>', shareme.consts.broad_port))
            print("SEND BROADCAST")
            time.sleep(sleep_time)
            if (self.__client):
                break
        print("RECEIVED CONNECTION")
        self._closeUDP()
        del self.__broad
        