import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, Box

class Crypto():
    def __init__(self, client_or_server):
        # 1 means client
        if (client_or_server):
            self.__key=nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
            self.__boxS = nacl.secret.SecretBox(self.__key)
        self._genAsym()

    def setKey(self, k):
        self.__key=k
        self.__boxS = nacl.secret.SecretBox(self.__key)

    def encryptSym(self, msg):
        return self.__boxS.encrypt(msg)
    
    def decryptSym(self, msg):
        return self.__boxS.decrypt(msg)

    def _genAsym(self):
        self.__privm = PrivateKey.generate()
        self.__pubm = self.__privm.public_key
    
    def otherPub(self, other_pub):
        self.__otherk=other_pub
        self.__boxA=Box(self.__privm, self.__otherk)

    def encryptKey(self):
        return self.encryptAsym(self.__key)

    def encryptAsym(self, msg):
        return self.__boxA.encrypt(msg)
    
    def decryptAsym(self, msg):
        return self.__boxA.decrypt(msg)

    @property
    def pubm(self):
        return self.__pubm
