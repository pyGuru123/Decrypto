import unittest

from decrypto.src.ascii_cipher import AsciiCipher
from tests import random_string

class TestAsciiCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = AsciiCipher()
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Ascii Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()