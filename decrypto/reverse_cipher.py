class ReverseCipher:
    def __init__(self):
        """ This is a python implementation of Reverse Cipher"""
        self.result = None

    def encrypt(self, msg: str) -> str:
        result = msg[::-1]
        return result

    def decrypt(self, msg: str) -> str:
        result = self.encrypt(msg)
        return result