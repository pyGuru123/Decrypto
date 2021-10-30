import unittest
import random

from decrypto.src.affine_cipher import AffineCipher
from tests import random_string

class TestAffineCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        a = random.choice((3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25))
        b = random.randint(1, 100)

        cipher = AffineCipher()
        data:str = random_string().upper()
        encrypted = cipher.encrypt(data, a, b)
        decrypted = cipher.decrypt(encrypted, a, b)

        self.assertEqual(data, decrypted, "Affine Cipher problem in encryption/decryption")

if __name__ == '__main__':
    unittest.main()