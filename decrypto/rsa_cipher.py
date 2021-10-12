
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
#pip3 install -U PyCryptodome
class RSACipher:
    def __init__(self):
        """ This is a python implementation of RSA Cipher. More about it can
        be read here : https://simple.wikipedia.org/wiki/RSA_algorithm"""
    @staticmethod
    def encrypt(self, text: str, AES256key : str) -> str:
        BLOCK_SIZE = AES.block_size
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        private_key = hashlib.sha256(AES256key.encode("utf-8")).digest()
        raw = pad(text)
        raw = raw.encode("utf8")
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode()

    @staticmethod
    def decrypt(self, text: str,  AES256key : str ) -> str:
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        private_key = hashlib.sha256(AES256key.encode("utf-8")).digest()
        data = base64.b64decode(text)
        BLOCK_SIZE = AES.block_size
        iv = data[:BLOCK_SIZE]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(data[BLOCK_SIZE:])).decode()