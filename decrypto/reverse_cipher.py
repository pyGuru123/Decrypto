class ReverseCipher:
    def __init__(self):
        """This is a python implementation of Reverse Cipher"""

    @staticmethod
    def encrypt(msg: str) -> str:
        result = msg[::-1]
        return result

    @staticmethod
    def decrypt(msg: str) -> str:
        result = msg[::-1]
        return result
