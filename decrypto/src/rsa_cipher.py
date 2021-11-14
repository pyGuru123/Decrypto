import random

class RSACipher():
    def __init__(self):
        """This is a python implementation of RSA Cipher"""

    @staticmethod
    def get_totient(p, q):
        return (p - 1) * (q - 1)

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return RSACipher.gcd(b, a % b)

    @staticmethod
    def get_e(totient):
        e = random.randint(2, totient - 1)
        while RSACipher.gcd(e, totient) != 1:
            e = random.randint(2, totient - 1)

        return e

    @staticmethod
    def modular_inverse(a, m):
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1

    @staticmethod
    def generate_keys(p, q):
        p = p
        q = q
        n = p * q
        totient = RSACipher.get_totient(p, q)
        # e = RSACipher.get_e(totient)
        e = 563
        d = RSACipher.modular_inverse(e, totient)

        keys = {
            'public_key' : (n, e),
            'private_key' : (p, q, d)
        }

        return keys

    @staticmethod
    def encrypt(msg, public_key):
        n, e = public_key
        if isinstance(msg, int):
            result = (msg ** e) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** e) % n)

        return result

    @staticmethod
    def decrypt(msg, private_key):
        p, q, d = private_key
        n = p * q
        if isinstance(msg, int):
            result = (msg ** d) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** d) % n)

        return result
