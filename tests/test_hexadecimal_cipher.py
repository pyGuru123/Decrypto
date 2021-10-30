import unittest

from decrypto.src.hexadecimal_cipher import HexadecimalCipher
from tests import random_string

class TestHexadecimalCipher(unittest.TestCase):
    pass
    # PROBLEM IN ENCRYPTING AND DECRYPTING
    # def test_encrypt_decrypt(self):
    #     cipher = HexadecimalCipher()
    #     data:str = random_string()

    #     encrypted = cipher.encrypt(data)
    #     decrypted = cipher.decrypt(encrypted)

    #     self.assertEqual(data, decrypted, "Hexadecimal Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()