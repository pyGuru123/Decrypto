import string


class AtbashCipher:
    def __init__(self) -> None:
        """This is a python implementation of AtBashCipher Cipher"""

        alpha = string.ascii_uppercase
        self.lookup_dict = {alpha[i]: alpha[::-1][i] for i in range(26)}

    def encrypt(self, msg: str) -> str:
        result = ''
        for ch in msg.upper():
            result += self.lookup_dict.get(ch, ch)

        return result

    def decrypt(self, msg: str) -> str:
        result = self.encrypt(msg)
        return result
