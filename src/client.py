import socket
import consts

class Client():
    def __init__(self, timeout=consts.timeout):
        self.__timeout=timeout
        self.__createSocket()
        self.__setOpts(timeout)

    def __setOpts(self, timeout):
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.__s.settimeout(timeout)

    def __createSocket(self):
        self.__s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.settimeout(self.__timeout)
    
    def close(self):
        self.__s.close()

    def _bind(self, ip, port):
        self.__ip_bind=ip
        self.__port_bind=port
        self.__s.bind((ip, port))

    def receiveBroadcast(self):
        self._bind((consts.all_ip, consts.service_port))
        while(True):
            data, addr = self.__s.recvfrom(1024)
            if (data==b"Hello lets share!!"):
                self.__ip_bind=addr.decode(consts.encoding)
                self.__port_bind=consts.service_port
                self.close()
                break
        self.__createSocket()
        self.__s.connect((addr, consts.service_port))

    def receive(self):
        return self.__s.recv(consts.buffer)

    @property
    def timeout(self):
        return self.__timeout

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
