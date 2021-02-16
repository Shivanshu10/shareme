from os import confstr_names
import consts
import socket
class Server():
    def __init__(self, timeout=consts.timeout):
        self.__createSocket()
        self.__timeout=timeout
        self.__setOpts(timeout)

    def __createSocket(self):
        self.__s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.settimeout(self.__timeout)

    def __setOpts(self, timeout):
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__s.settimeout(timeout)
    
    def _bind(self, ip, port):
        self.__ip_bind=ip
        self.__port_bind=port
        self.__s.bind((ip, port))

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

    def send(self, ch):
        self.__client.sendall(ch)

    def close(self):
        if (self.__client):
            self.__closeServer()
        self.__s.close()

    def _startServer(self):
        self._bind(consts.all_ip, consts.service_port)
        self.__s.listen(1)
        conn, addr=self.__s.accept()
        self.__client=conn
        self.__ip_bind=addr.decode('utf-8')
    
    def __closeServer(self):
        self.__client.close()
    
    def sendBroadcast(self):
        self.__s.sendto(b"Hello lets share!!", ('<broadcast>', consts.service_port))
        self.close()
        self._startServer()