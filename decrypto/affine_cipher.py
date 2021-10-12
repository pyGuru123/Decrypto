class AffineCipher:

    def __init__(self):
        """This is a python implementation of Affine Cipher"""

    # Euclidean Algorithm for finding modular inverse
    @staticmethod
    def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y

    # Modular Inverse
    @staticmethod
    def modinv(a, m):
        gcd, x, y = AffineCipher.egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    @staticmethod
    def encrypt(msg: str, a: int, b: int) -> str:
        return ''.join([ chr((( a*(ord(t) - ord('A')) + b ) % 26)
                  + ord('A')) for t in msg.upper().replace(' ', '') ])

    @staticmethod
    def decrypt(msg: str, a:int, b:int) -> str:
        return ''.join([ chr(((AffineCipher.modinv(a, 26)*(ord(c) - ord('A') - b))
                    % 26) + ord('A')) for c in msg ])
   

print (AffineCipher.decrypt("UBBAHK CAPJKX",17,20))
