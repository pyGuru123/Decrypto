class VigenereCipher:
    def __init__(self) -> None:
        """This is a python implementation of Vigenere Cipher"""

    def modify_key(self, msg: str, key: str) -> str:
        '''Generates the key in a cyclic manner until it's length equal to the 
            length of text'''

        if len(msg) > len(key):
            for i in range(len(msg) - len(key)):
                key += key[i % len(key)]

        return key

    def encrypt(self, msg: str, key: str) -> str:
        msg, key = msg.upper(), key.upper()
        key = self.modify_key(msg, key)

        encrypted_words = []
        curr_key_index = 0
        for text in msg.split():
            result = ''
            for i in range(len(text)):
                x = (ord(text[i]) + ord(key[curr_key_index])) % 26
                x += ord('A')
                result += chr(x)
                curr_key_index += 1
            encrypted_words.append(result)

        return ' '.join(encrypted_words).lower()

    def decrypt(self, msg: str, key: str) -> str:
        msg, key = msg.upper(), key.upper()
        key = self.modify_key(msg, key)

        decrypted_words = []
        curr_key_index = 0
        for word in msg.split():
            result = ''
            for i in range(len(word)):
                x = (ord(word[i]) - ord(key[curr_key_index]) + 26) % 26
                x += ord('A')
                result += chr(x)
                curr_key_index += 1
            decrypted_words.append(result)

        return ' '.join(decrypted_words).lower()
