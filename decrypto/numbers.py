# This module contains some basic encryption decryption methods related to numbers

import string
import webbrowser

class BinaryCipher:
	def __init__(self):
		''' This is a python implementation of Binary Cipher'''
		self.url = 'https://en.wikipedia.org/wiki/Binary-to-text_encoding'

	def about(self):
		'''Read about Binary Cipher online'''
		
		webbrowser.open(self.url) 

	def encrypt(self, msg: [int, str]) -> str:
		result = None

		if isinstance(msg, int):
			binary = bin(msg)
			result = int(str(binary)[2:])

		elif isinstance(msg, str):
			result = ''
			for ele in msg:
				value = ord(ele)
				binary_value = bin(value) + ' '
				result += binary_value[2:]

		return result

	def decrypt(self, msg: [int, str]) -> str:
		result = None

		if isinstance(msg, int):
			result = int(str(msg), 2)

		elif isinstance(msg, str):
			result = ''
			splitted_list = msg.split()
			for ele in splitted_list:
				value = int(ele, 2)
				result += chr(value)

		return result


class OctalCipher:
	def __init__(self):
		''' This is a python implementation of HexaDecimal Cipher'''

		self.url = 'https://en.wikipedia.org/wiki/Hexadecimal'

	def about(self):
		'''Read about Binary Cipher online'''
		
		webbrowser.open(self.url) 

	def encrypt(self, msg: [int, str] ) -> str:
		result = None

		if isinstance(msg, int):
			octal = oct(msg)
			result = int(str(octal)[2:])

		elif isinstance(msg, str):
			result = ''
			for ele in msg:
				value = ord(ele)
				octal_value = oct(value) + ' '
				result += octal_value[2:]

		return result

	def decrypt(self, msg: [int, str] ) -> str:
		result = None

		if isinstance(msg, int):
			result = int(str(msg), 8)

		elif isinstance(msg, str):
			result = ''
			splitted_list = msg.split()
			for ele in splitted_list:
				value = int(ele, 8)
				result += chr(value)

		return result


class HexadecimalCipher:
	def __init__(self):
		''' This is a python implementation of HexaDecimal Cipher'''

		self.url = 'https://en.wikipedia.org/wiki/Hexadecimal'

	def about(self):
		'''Read about Binary Cipher online'''
		
		webbrowser.open(self.url) 

	def encrypt(self, msg: [int, str] ) -> str:
		result = None

		if isinstance(msg, int):
			hexadecimal = hex(msg)
			result = str(hexadecimal)[2:]

		elif isinstance(msg, str):
			result = ''
			for ele in msg:
				value = ord(ele)
				hex_value = hex(value) + ' '
				result += hex_value[2:]
			try:
				result = int(result)
			except:
				result = result

		return result

	def decrypt(self, msg: [int, str] ) -> str:
		result = None

		if isinstance(msg, int):
			result = int(str(msg), 16)

		elif isinstance(msg, str):
			result = ''
			splitted_list = msg.split()
			for ele in splitted_list:
				value = int(ele, 16)
				result += str(value)

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