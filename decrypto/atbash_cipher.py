# Lookup Table for AtBash Cipher

lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


class AtBashCipher:
    def __init__(self) -> None:
        """This is a python implementation of AtBashCipher Cipher"""
    @staticmethod
    def encrypt(msg: str) -> str:
        cipher = ''
        word = msg.upper()
        for letter in word:
            # checks for space
            if(letter != ' '):
                # adds the corresponding letter from the lookup_table
                cipher += lookup_table[letter]
            else:
                # adds space
                cipher += ' '

        return cipher

    @staticmethod
    def decrypt(msg: str) -> str:
        cipher = ''
        word = msg.upper()
        for letter in word:
            # checks for space
            if(letter != ' '):
                # adds the corresponding letter from the lookup_table
                cipher += lookup_table[letter]
            else:
                # adds space
                cipher += ' '

        return cipher
