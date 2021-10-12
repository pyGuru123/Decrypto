from decrypto.rsa_cipher import RSACipher
import unittest
class TestSum(unittest.TestCase):
    def Validation(self):
        """
        Test that it can sum a list of integers
        """
        text = "Nice to meet you"
        mykey = "CODINGBEAST"
        result = RSACipher().encrypt(self, text= text, AES256key = mykey)
        decrypted = RSACipher().decrypt(self, text = result, AES256key = mykey)
        self.assertEqual(decrypted, text)

if __name__ == '__main__':
    unittest.main()
