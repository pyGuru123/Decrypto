from Crypto.Util.number import *

class RSACipher:
    def __init__(self):
        """ This is a python implementation of RSACipher """

    @staticmethod
    def encrypt(plaintext: str) -> str:
        p = int(input("p : "))
        q = int(input("q : "))
        N = p * q
        e = 65537 #only for this exponent, but you can change it
        m = bytes_to_long(bytes(plaintext, 'utf8'))
        c = pow(m, e, N)
        print(f"Encryption output :\nN : {N}\nc : {c}\ne : {e}")

    @staticmethod
    def decrypt(p, q, e, c):
        print("You can check prime p and q factorial from computing N value here : https://factordb.com/")
        N = p * q
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
        m = pow(c, d, N)
        plaintext = long_to_bytes(m)
        print(f"plaintext : {plaintext}")