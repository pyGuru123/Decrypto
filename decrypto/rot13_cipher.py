class ROT13Cipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, message):
        cipher = ''
        for letter in message.upper():
            # checking for space
            if(letter != ' '):
                num = chr((ord(letter) - ord('A') + 13 ) % 26 + ord('A'))
                cipher += num
            else:
                # adds space
                cipher += ' '
        return cipher

    def decrypt(self, message):
        decipher = ''
        for letter in message.upper():
            # checks for space
            if(letter != ' '):
                num = chr(((ord(letter) - ord('A') - 13 + 26) % 26) + ord('A'))
                decipher += num
            else:
                # adds space
                decipher += ' '
        return decipher