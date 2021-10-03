# Octal Cipher implimentation

class OctalCipher:
    def __init__(self):
        ''' This is a python implementation of Binary Cipher. More about it can
        be read here : https://en.wikipedia.org/wiki/Octal'''

    def encrypt(self, msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            octal = oct(msg)
            result = int(str(octal)[2:])

        elif isinstance(msg, str):
            result = ''
            for ele in msg:
                value = ord(ele)
                octal_value = oct(value) + ' '
                result += octal_value[2:]

        return result

    def decrypt(self, msg: [int, str]) -> str:
        result = None

        if isinstance(msg, int):
            result = int(str(msg), 8)

        elif isinstance(msg, str):
            result = ''
            splitted_list = msg.split()
            for ele in splitted_list:
                value = int(ele, 8)
                result += chr(value)

        return result
