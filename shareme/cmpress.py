import zlib

class Compresser():
    @staticmethod
    def compress(s, level=4):
        return zlib.compress(s, level)

    @staticmethod
    def decompress(cmpressed_str):
        return zlib.decompress(cmpressed_str)