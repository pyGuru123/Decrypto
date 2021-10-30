import unittest

from decrypto.src.roman_numeral_cipher import RomanNumeralCipher
from tests import random_string

class TestRomanNumeral(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = RomanNumeralCipher()
        data:int = int(random_string(length=5, ascii=False))

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted)

        self.assertEqual(data, decrypted, "Roman Numeral Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()