import consts
import socket
class Server():
    def __init__(self, ip=consts.all_ip, port=consts.service_port, timeout=consts.timeout):
        self.__ip_bind=ip
        self.__port_bind=port
        self.__s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__setOpts(timeout)

    def __setOpts(self, timeout):
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__s.settimeout(timeout)
    
    def _bind(self, ip, port):
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

    def send():
        pass

    def close(self):
        self.__s.close()

    def sendBroadcast(self):
        self.__s.sendto(b"Hello lets share!!", ('<broadcast>', consts.service_port))
