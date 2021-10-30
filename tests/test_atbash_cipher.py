import unittest

from decrypto.src.atbash_cipher import AtbashCipher
from tests import random_string

class TestAtbashCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = AtbashCipher()
        data:str = random_string().upper()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Atbash Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()