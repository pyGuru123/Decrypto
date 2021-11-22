class ROT13Cipher:
    def __init__(self) -> None:
        '''This is python implementation of ROT13 Cipher'''
        pass

    def encrypt(self, message: str) -> str:
        result = ''
        for ch in message.upper():
            if ch.isalpha():
                encoded = chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
                result += encoded
            else:
                result += ch
        return result

    def decrypt(self, message: str) -> str:
        return self.encrypt(message)
