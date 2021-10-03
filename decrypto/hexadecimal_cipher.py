# Hexadecimal Cipher implimentation

class HexadecimalCipher:
    def __init__(self):
        ''' This is a python implementation of Binary Cipher. More about it can
        be read here : https://en.wikipedia.org/wiki/Hexadecimal'''

    def encrypt(self, msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            hexadecimal = hex(msg)
            result = str(hexadecimal)[2:]

        elif isinstance(msg, str):
            result = ''
            for ele in msg:
                value = ord(ele)
                hex_value = hex(value) + ' '
                result += hex_value[2:]
            try:
                result = int(result)
            except:
                result = result

        return result

    def decrypt(self, msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            result = int(str(msg), 16)

        elif isinstance(msg, str):
            result = ''
            splitted_list = msg.split()
            for ele in splitted_list:
                value = int(ele, 16)
                result += str(value)

        return result