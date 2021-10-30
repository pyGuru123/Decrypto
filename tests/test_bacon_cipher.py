import unittest

from decrypto.src.bacon_cipher import BaconCipher
from tests import random_string

class TestBaconCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = BaconCipher()
        data:str = random_string(digits=False).upper()

        encrypted = cipher.encrypt(data)
        decrypted = cipher.decrypt(encrypted).replace(' ', '')

        self.assertEqual(data, decrypted, "Bacon Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()