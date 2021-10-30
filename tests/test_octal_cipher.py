import unittest

from decrypto.src.octal_cipher import OctalCipher
from tests import random_string

class TestOctalCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = OctalCipher()
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Octal Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()