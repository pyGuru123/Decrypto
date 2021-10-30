import string
import secrets

def random_string(length:int = 1024, ascii:bool = True, digits:bool = True) -> str:
    """Generate a random alphanumeric string of size `length`
    
    Keyword arguments:
    Argument: length:int (defaults to 128), 
    Return: string
    """
    alphabet = []
    if ascii: alphabet += string.ascii_letters
    elif digits: alphabet += string.digits
    else: raise SyntaxError("bool or digits should either be True")
    return ''.join(secrets.choice(alphabet) for i in range(length))


# General testing template for ciphers
"""
import unittest

from decrypto.src.cipher import Cipher
from tests import random_string

class TestCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = Cipher()
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "<Cipher> Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()
"""