import unittest
import random

from decrypto.src.caesar_cipher import CaesarCipher
from tests import random_string

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = CaesarCipher()
        data:str = random_string().lower()
        key = random.randint(1, 27)

        encrypted = cipher.encrypt(data, key)
        decrypted = cipher.decrypt(encrypted, key)

        self.assertEqual(data, decrypted, "Caesar Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()