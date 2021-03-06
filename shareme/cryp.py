import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, Box, PublicKey
from nacl.encoding import Base64Encoder
import base64
class Crypto():
    def __init__(self, client_or_server):
        # 1 means client
        self._genAsym()

    def _genAsym(self):
        self.__privm = PrivateKey.generate()
        self.__pubm = self.__privm.public_key
    
    def encodedPub(self):
        return self.__pubm.encode(Base64Encoder)

    def decodedPub(self, pub):
        return base64.b64decode(pub.decode('utf-8'))

    def otherPub(self, other_pub):
        other_pub=self.decodedPub(other_pub)
        self.__otherk=PublicKey(other_pub)
        self.__boxA=Box(self.__privm, self.__otherk)

    def encryptAsym(self, msg):
        return self.__boxA.encrypt(msg)
    
    def decryptAsym(self, msg):
        return self.__boxA.decrypt(msg)

    @property
    def pubm(self):
        return self.__pubm
