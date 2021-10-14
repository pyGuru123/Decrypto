class BaconCipher:
    def __init__(self):
        '''This is python implementation of Bacon Cipher'''

        self.bacon_dict = {
            'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba',
            'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab',
            'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa',
            'J': 'abaab', 'K': 'ababa', 'L': 'ababb',
            'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
            'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab',
            'S': 'baaba', 'T': 'baabb', 'U': 'babaa',
            'V': 'babab', 'W': 'babba', 'X': 'babbb',
            'Y': 'bbaaa', 'Z': 'bbaab'
        }

        self.reverse_bacon = {
            self.bacon_dict[key]: key for key in self.bacon_dict
        }

    def encrypt(self, message: str) -> str:
        '''Encrypt plain text based upon the above bacon dict'''
        result = ''
        for ch in message.upper():
            result += self.bacon_dict.get(ch, '')
            result += ' '
        return result.strip()

    def decrypt(self, message: str) -> str:
        '''Decrypt plain text based upon the above reverse bacon dict'''
        result = ''
        for encoded in message.split(' '):
            result += self.reverse_bacon.get(encoded, ' ')
        return result
