class VigenereCipher:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encrypt(msg: str, key: str) -> str:
        msg, key  = msg.upper(), key.upper() 
        if len(msg) > len(key):
            # Generates the key in a cyclic manner until it's length equal to the length of text
            for i in range(len(msg) - len(key)):
                key += key[i % len(key)]
        encrypted_words = []
        for text in msg.split():
            result = ''
            for i in range(len(text)):
                x = (ord(text[i]) + ord(key[i])) % 26
                x += ord('A')
                result+= chr(x)
            encrypted_words.append(result)
        return ' '.join(encrypted_words)

    @staticmethod
    def decrypt(msg: str,key: str) -> str:
        msg, key  = msg.upper(), key.upper() 
        if len(msg) > len(key):
            # Generates the key in a cyclic manner until it's length equal to the length of msg
            for i in range(len(msg) - len(key)):
                key += key[i % len(key)]
        decrypted_words = []
        for word in msg.split():
            result = ''     
            for i in range(len(word)):
                x = (ord(word[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                result += chr(x)
            decrypted_words.append(result)
        return ' '.join(decrypted_words)