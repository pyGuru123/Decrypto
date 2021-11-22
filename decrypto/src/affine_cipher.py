class AffineCipher:
    def __init__(self):
        """This is a python implementation of Affine Cipher"""
        pass

    @staticmethod
    def modinv(a: int, m: int):
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1

    @staticmethod
    def encrypt(msg: str, a: int, b: int) -> str:
        result = ''
        for ch in msg.upper():
            if ch.isalpha():
                result += chr(((a * (ord(ch) - ord('A')) + b) % 26)
                              + ord('A'))
            else:
                result += ch
        return result

    @staticmethod
    def decrypt(msg: str, a: int, b: int) -> str:
        result = ''
        for ch in msg.upper():
            if ch.isalpha():
                result += chr(((AffineCipher.modinv(a, 26) * (ord(ch)
                            - ord('A') - b)) % 26) + ord('A'))
            else:
                result += ch
        return result
