class MorseCodeCipher:
    def __init__(self):
        """ This is a python implementation of MorseCode Cipher"""

        self.morse_dict = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-',
            'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--',
            'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ',': '--..--', '.': '.-.-.-',
            '?': '..--..', ' ': '/', '-': '-....-',
            '(': '-.--.', ')': '-.--.-'
        }

        self.reverse_morse = {
            self.morse_dict[key]: key for key in self.morse_dict
        }

    def encrypt(self, text: str) -> str:
        result = ''
        for ch in text.upper():
            result += self.morse_dict.get(ch, ch)
            result += ' '

        return result.strip()

    def decrypt(self, text: str) -> str:
        result = ''
        for ch in text.split():
            result += self.reverse_morse.get(ch, ch)

        return result
