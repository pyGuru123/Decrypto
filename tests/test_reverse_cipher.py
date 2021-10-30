import unittest

from decrypto.src.reverse_cipher import ReverseCipher
from tests import random_string

class TestReverseCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = ReverseCipher
        data:str = random_string()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Reverse Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()