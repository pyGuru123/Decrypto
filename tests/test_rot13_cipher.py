import unittest

from decrypto.src.rot13_cipher import ROT13Cipher
from tests import random_string

class TestROT13Cipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = ROT13Cipher()
        data:str = random_string().upper()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "ROT13 Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()