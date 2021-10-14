import base64


class Base64Cipher:
    def __init__(self) -> None:
        """This is a python implementation of Base64 Cipher"""

    @staticmethod
    def encrypt(msg: str) -> str:
        encoded = msg.encode('ascii')
        base64_bytes = base64.b64encode(encoded)
        result = base64_bytes.decode("ascii")
        return result

    @staticmethod
    def decrypt(msg: str) -> str:
        encoded = msg.encode('ascii')
        sample_string_bytes = base64.b64decode(encoded)
        result = sample_string_bytes.decode("ascii")
        return result
