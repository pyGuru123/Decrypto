import unittest

from decrypto.src.vigenere_cipher import VigenereCipher
from tests import random_string

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = VigenereCipher()
        data:str = random_string().lower()
        key:str = random_string(256)

        encrypted = cipher.encrypt(data, key)
        decrypted = cipher.decrypt(encrypted, key)

        self.assertEqual(data, decrypted, "Vigenere Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()