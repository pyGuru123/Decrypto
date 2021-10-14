class AffineCipher:

    def __init__(self):
        """This is a python implementation of Affine Cipher"""

    @staticmethod
    def egcd(a, b):
        '''Euclidean Algorithm for finding modular inverse'''
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    @staticmethod
    def modinv(a, m):
        '''Modular Inverse'''
        gcd, x, y = AffineCipher.egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    @staticmethod
    def encrypt(msg: str, a: int, b: int) -> str:
        result = ''
        for ch in msg.upper():
            if ch.isalpha():
                result += chr(((a * (ord(ch) - ord('A')) + b) % 26)
                              + ord('A'))
            else:
                result += ch
        return result

    @staticmethod
    def decrypt(msg: str, a: int, b: int) -> str:
        result = ''
        for ch in msg.upper():
            if ch.isalpha():
                result += chr(((AffineCipher.modinv(a, 26) * (ord(ch)
                            - ord('A') - b)) % 26) + ord('A'))
            else:
                result += ch
        return result
