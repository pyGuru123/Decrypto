class  BaconCipher:
    def __init__(self) -> None:
        self.baco_dict = { 
                            'A':'aaaaa', 'B':'aaaab', 'C':'aaaba',
                            'D':'aaabb', 'E':'aabaa', 'F':'aabab', 
                            'G':'aabba', 'H':'aabbb', 'I':'abaaa', 
                            'J':'abaab', 'K':'ababa', 'L':'ababb', 
                            'M':'abbaa', 'N':'abbab', 'O':'abbba',
                            'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 
                            'S':'baaba', 'T':'baabb', 'U':'babaa', 
                            'V':'babab', 'W':'babba', 'X':'babbb', 
                            'Y':'bbaaa', 'Z':'bbaab'
        }
        self.reverse_baco = { 
            self.baco_dict[key] : key for key in self.baco_dict }

    def encrypt(self, message : str) -> str:
        cipher = ''
        for letter in message.upper():
            # checks for space
            if(letter != ' '):
                # adds the ciphertext corresponding to the 
                # plaintext from the dictionary
                cipher += self.baco_dict[letter]
            else:
                # adds space
                cipher += ' '
        return cipher

    def decrypt(self,message):
        decipher = ''
        i = 0
        while True :
            if(i < len(message)-4):
                # extracting a set of ciphertext
                # from the message which is of size 5
                substr = message[i:i + 5]
                # checking for space as the first 
                # character of the substring
                if(substr[0] != ' '):
                    decipher += self.reverse_baco[substr]
                    i += 5 # to get the next set of ciphertext
                else:
                    # adds space
                    decipher += ' '
                    i += 1 # index next to the space
            else:
                break
        return decipher
