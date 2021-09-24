# This module contains basic encryption and decryption methods

import string
import webbrowser

class AsciiCipher:
	def __init__(self):
		''' This is a python implementation of Ascii Cipher'''

		self.url = 'http://www.asciitable.com/'

	def about(self):
		'''Read about Ascii Cipher online'''

		webbrowser.open(self.url) 

	def encrypt(self, msg: str) -> str:
		result = ''
		for ele in msg:
			value = ord(ele)
			result += f'{value} '

		return result

	def decrypt(self, msg: str) -> str:
		result = ''
		for ele in msg.split():
			value = chr(int(ele))
			result += value

		return result 

class CeaserCipher:
	def __init__(self):
		''' This is a python implementation of Ceaser Cipher'''

		self.alphabets = string.ascii_lowercase
		self.url = 'https://en.wikipedia.org/wiki/Caesar_cipher'

	def about(self):
		'''Read about Ceaser Cipher online'''

		webbrowser.open(self.url) 

	def encrypt(self, msg: str, key: int) -> str:
		result = ''
		for ele in msg.lower():
			pos = self.alphabets.find(ele)
			new = (pos + key) % 26
			result += self.alphabets[new]

		return result

	def decrypt(self, msg: str, key: int) -> str:
		result = ''
		for ele in msg.lower():
			pos = self.alphabets.find(ele)
			new = (pos - key) % 26
			result += self.alphabets[new]

		return result

class MorseCodeCipher:
	def __init__(self):
		''' This is a python implementation of Roman Numeral Cipher'''

		self.morse_dict = { 'A':'.-', 'B':'-...', 
							'C':'-.-.', 'D':'-..', 'E':'.', 
							'F':'..-.', 'G':'--.', 'H':'....', 
							'I':'..', 'J':'.---', 'K':'-.-', 
							'L':'.-..', 'M':'--', 'N':'-.', 
							'O':'---', 'P':'.--.', 'Q':'--.-', 
							'R':'.-.', 'S':'...', 'T':'-', 
							'U':'..-', 'V':'...-', 'W':'.--', 
							'X':'-..-', 'Y':'-.--', 'Z':'--..', 
							'1':'.----', '2':'..---', '3':'...--', 
							'4':'....-', '5':'.....', '6':'-....', 
							'7':'--...', '8':'---..', '9':'----.', 
							'0':'-----', ',':'--..--', '.':'.-.-.-', 
							'?':'..--..', '/':'-..-.', '-':'-....-', 
							'(':'-.--.', ')':'-.--.-'
						}

		self.reverse_morse = {self.morse_dict[key]:key for key in self.morse_dict}
		self.url = 'https://www.britannica.com/topic/Morse-Code'

	def about(self):
		'''Read about Morse Code Cipher online'''
		webbrowser.open(self.url) 

	def encrypt(self, text: str) -> str:
		result = ''

		for ch in text.upper():
			if ch != ' ':
				val = self.morse_dict.get(ch, ch)
				result += (val + ' ')
			else:
				result += ' '

		return result

	def decrypt(self, text: str) -> int:
		text = text.strip(' ') + ' '
		result = ''

		i = 0
		char = ''
		space_ct = 0

		while i < len(text):
			if text[i] == ' ':
				if space_ct == 0:
					result += self.reverse_morse.get(char, char)
					space_ct += 1
					char = ''
				else:
					space_ct += 1
			else:
				if space_ct > 0:
					result += ' ' * (space_ct - 1)
					space_ct = 0
				char += text[i]

			i += 1

		return result


class ReverseCipher:
	def __init__(self):
		''' This is a python implementation of Reverse Cipher'''

		self.result = None
		self.url = 'https://inventwithpython.com/hacking/chapter5.html'

	def about(self):
		'''Read about Reverse Cipher online'''
		
		webbrowser.open(self.url) 

	def encrypt(self, msg: str) -> str:
		result = msg[::-1]
		return result

	def decrypt(self, msg: str) -> str:
		result = self.encrypt(msg)
		return result