class BinaryCipher:
    def __init__(self):
        """ This is a python implementation of Binary Cipher. More about it can
        be read here : https://en.wikipedia.org/wiki/Binary-to-text_encoding"""

    @staticmethod
    def encrypt(msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            binary = bin(msg)
            result = int(str(binary)[2:])

        elif isinstance(msg, str):
            result = ''
            for ele in msg:
                value = ord(ele)
                binary_value = bin(value) + ' '
                result += binary_value[2:]

        return result

    @staticmethod
    def decrypt(msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            result = int(str(msg), 2)

        elif isinstance(msg, str):
            result = ''
            for ele in msg.split():
                value = int(ele, 2)
                result += chr(value)

        return result
