import random

class RSACipher():
    def __init__(self):
        """This is a python implementation of RSA Cipher"""

    @staticmethod
    def get_totient(p: int, q: int):
        return (p - 1) * (q - 1)

    @staticmethod
    def gcd(a: int, b: int):
        if b == 0:
            return a
        else:
            return RSACipher.gcd(b, a % b)

    @staticmethod
    def get_e(totient: int):
        e = random.randint(2, totient - 1)
        while RSACipher.gcd(e, totient) != 1:
            e = random.randint(2, totient - 1)

        return e

    @staticmethod
    def modular_inverse(a: int, m: int):
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1

    @staticmethod
    def generate_keys(p: int, q: int):
        p = p
        q = q
        n = p * q
        totient = RSACipher.get_totient(p, q)
        e = RSACipher.get_e(totient)
        d = RSACipher.modular_inverse(e, totient)

        keys = {
            'public_key' : (n, e),
            'private_key' : (p, q, d)
        }

        return keys

    @staticmethod
    def encrypt(msg: str, public_key: tuple):
        n, e = public_key
        if isinstance(msg, int):
            result = (msg ** e) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** e) % n)

        return result

    @staticmethod
    def decrypt(msg: str, private_key: tuple):
        p, q, d = private_key
        n = p * q
        if isinstance(msg, int):
            result = (msg ** d) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** d) % n)

        return result
