import socket
import shareme.consts

class Client():
    def __init__(self):
        self.__createSocketTCP()
        self.__createSocketUDP()
        self.__setOpts()

    def __setOpts(self):
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
    def __createSocketTCP(self):
        self.__s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def __createSocketUDP(self):
        self.__broad=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
    def close(self):
        self.__s.close()

    def _bind(self, ip, port):
        self.__ip_bind=ip
        self.__port_bind=port
        self.__broad.bind((ip, port))

    def _closeUDP(self):
        self.__broad.close()

    def receiveBroadcast(self):
        self._bind(shareme.consts.all_ip, shareme.consts.broad_port)
        while(True):
            data, addr = self.__broad.recvfrom(1024)
            if (data==b"Hello lets share!!"):
                print("RECEIVED BROADCAST")
                print(addr)
                self.__ip_bind=addr[0]
                self.__port_bind=shareme.consts.service_port
                self._closeUDP()
                del self.__broad
                break
        self.__s.connect((addr[0], shareme.consts.service_port))
        print("CONNECT TO SERVER")

    def receive(self):
        return self.__s.recv(shareme.consts.buffer)

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
