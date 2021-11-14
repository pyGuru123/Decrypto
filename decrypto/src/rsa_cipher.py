import random

class RSACipher():
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.totient = self.get_totient()
        self.e = self.get_e()
        self.d = self.modular_inverse(self.e, self.totient)

    def get_totient(self):
        return (self.p - 1) * (self.q - 1)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def get_e(self):
        e = random.randint(2, self.totient - 1)
        while self.gcd(e, self.totient) != 1:
            e = random.randint(2, self.totient - 1)

        return e

    def modular_inverse(self, a, m):
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1

    def generate_keys(self):
        keys = {
            'public_key' : (self.n, self.e),
            'private_key' : (self.p, self.q, self.d)
        }

        return keys

    def encrypt(self, msg, public_key):
        n, e = public_key
        if isinstance(msg, int):
            result = (msg ** e) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** e) % n)

        return result

    def decrypt(self, msg, private_key):
        p, q, d = private_key
        n = p * q
        if isinstance(msg, int):
            result = (msg ** d) % n
        elif isinstance(msg, str):
            result = ''
            for ch in msg:
                result += chr((ord(ch) ** d) % n)

        return result

cipher = RSACipher(53, 59)
message = 'hello world'
keys = cipher.generate_keys()
encrypted = cipher.encrypt(message, keys['public_key'])
decrypted = cipher.decrypt(message, keys['private_key'])
print(keys)
print(encrypted)
print(decrypted)



# 