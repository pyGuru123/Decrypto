class ScytaleCipher:
	def __init__(self):
		'''This is python implementation of Scytale Cipher'''

	def fix_text(self, text: str, key: int) -> str:
		padding = len(text) % key
		return text + '·' * (key - padding) if padding else text

	def encrypt(self, message: str, key: int) -> str:
		msg = self.fix_text(message.upper(), key)
		length = len(msg)
		cols = length//key
		result = ''

		for i in range(key):
			for j in range(cols):
				result += msg[j*key + i]

		return result

	def decrypt(self, message: str, key: int) -> str:
		msg = self.fix_text(message.upper(), key)
		length = len(msg)
		cols = length//key
		result = ''

		for i in range(cols):
			for j in range(key):
				result += msg[j*cols + i]

		return result
