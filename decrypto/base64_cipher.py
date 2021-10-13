import base64 as b


class Base64Cipher:
    def __init__(self) -> None:
        """This is a python implementation of Base64 Cipher"""

    @staticmethod
    def encrypt(msg: str) -> str:
        result = msg.encode('ascii')
        base64_bytes = b.b64encode(result)
        result = base64_bytes.decode("ascii")
        return result

    @staticmethod
    def decrypt(msg: str) -> str:
        result = msg.encode('ascii')
        sample_string_bytes = b.b64decode(result)
        result = sample_string_bytes.decode("ascii")
        return result
