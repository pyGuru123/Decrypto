import unittest

from decrypto.src.base64_cipher import Base64Cipher
from tests import random_string

class TestBase64Cipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = Base64Cipher()
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Base64 Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()