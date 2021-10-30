import unittest

from decrypto.src.binary_cipher import BinaryCipher
from tests import random_string

class TestBinaryCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = BinaryCipher()
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Binary Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()