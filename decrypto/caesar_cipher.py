import string


class CaesarCipher:
    def __init__(self):
        """This is a python implementation of Caesar Cipher"""
        self.alphabets = string.ascii_lowercase

    def encrypt(self, msg: str, key: int) -> str:
        result = ''
        for ele in msg.lower():
            pos = self.alphabets.find(ele)
            new = (pos + key) % 26
            result += self.alphabets[new]

        return result

    def decrypt(self, msg: str, key: int) -> str:
        result = ''
        for ele in msg.lower():
            pos = self.alphabets.find(ele)
            new = (pos - key) % 26
            result += self.alphabets[new]

        return result
