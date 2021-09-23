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

class BinaryCipher:
	def __init__(self):
		''' This is a python implementation of Binary Cipher'''

		self.url = 'https://en.wikipedia.org/wiki/Binary-to-text_encoding'

	def about(self):
		'''Read about Binary Cipher online'''

		webbrowser.open(self.url) 

	def encrypt(self, msg: str) -> str:
		result = ''
		for ele in msg:
			value = ord(ele)
			binary_value = bin(value) + ' '
			result += binary_value[2:]

		return result

	def decrypt(self, msg: str) -> str:
		result = ''
		splitted_list = msg.split()
		for ele in splitted_list:
			value = int(ele, 2)
			result += chr(value)

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


class RomanNumeralCipher:
	def __init__(self):
		''' This is a python implementation of Roman Numeral Cipher'''

		self.val = [
				1000, 900, 500, 400,
				100, 90, 50, 40,
				10, 9, 5, 4,
				1
		]

		self.syb = [
				"M", "CM", "D", "CD",
				"C", "XC", "L", "XL",
				"X", "IX", "V", "IV",
				"I"
		]

		self.url = 'https://www.britannica.com/topic/Roman-numeral'

	def about(self):
		'''Read about Roman Numeral Cipher online'''
		
		webbrowser.open(self.url) 

	def encrypt(self, num: int) -> str:
		result = ''

		if not isinstance(num, int):
			return 'Cannot cast to Roman cipher'

		i = 0
		while  num > 0:
			for _ in range(num // self.val[i]):
				result += self.syb[i]
				num -= self.val[i]
			i += 1

		return result

	def decrypt(self, msg: str) -> int:
		list_ = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
		num = 0

		for ele in list_:
			if ele in msg:
				msg = msg.replace(ele, '')
				num += self.val[self.syb.index(ele)]
		for ele in msg:
			num += self.val[self.syb.index(ele)]

		return num