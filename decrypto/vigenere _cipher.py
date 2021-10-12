class VigenereCipher:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encrypt(msg: str, key: str) -> str:
        if len(msg) <= len(key):
            return(key)
        else:
            # Generates the key in a cyclic manner until it's length equal to the length of msg
            for i in range(len(msg) - len(key)):
                key += key[i % len(key)]
        result = ''
        for i in range(len(msg)):
            x = (ord(msg[i]) + ord(key[i])) % 26
            x += ord('A')
            result+= chr(x)
        return result

    @staticmethod
    def decrypt(msg: str,key: str) -> str:
        if len(msg) <= len(key):
            return(key)
        else:
            # Generates the key in a cyclic manner until it's length equal to the length of msg
            for i in range(len(msg) - len(key)):
                key += key[i % len(key)]
        result = ''
        for i in range(len(msg)):
            x = (ord(msg[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            result += chr(x)
        return result