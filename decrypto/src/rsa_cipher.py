class RSACipher():
	def __init__(self, p, q):
		self.p = p
		self.q = q
		self.n = self.p * self.q
		self.phi = self.get_phi()

	def phi(self):
		return (self.p - 1) * (self.q - 1)