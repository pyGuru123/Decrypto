class AsciiCipher:
    def __init__(self):
        """This is a python implementation of Ascii Cipher"""

    def encrypt(self, msg: str) -> str:
        result = ''
        for ele in msg:
            value = ord(ele)
            result += f'{value} '

        return result

    def decrypt(self, msg: str) -> str:
        result = ''
        for ele in msg.split():
            value = chr(int(ele))
            result += value

        return result
