import string


class CaesarCipher:
    def __init__(self):
        """This is a python implementation of Caesar Cipher"""

    @staticmethod
    def encrypt(msg: str, key: int) -> str:
        result = ''
        for ele in msg.lower():
            pos = string.ascii_lowercase.find(ele)
            new = (pos + key) % 26
            result += string.ascii_lowercase[new]

        return result

    @staticmethod
    def decrypt(msg: str, key: int) -> str:
        result = ''
        for ele in msg.lower():
            pos = string.ascii_lowercase.find(ele)
            new = (pos - key) % 26
            result += string.ascii_lowercase[new]

        return result
