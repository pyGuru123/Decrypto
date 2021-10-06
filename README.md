# Decrypto

Decrypto is a light-weight python package to provide state of the art encrption and decryption techniques.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install decrypto.

```bash
pip install decrypto
```

## Usage

```python
from decrypto import MorseCodeCipher

data = 'Hello World 😊'

# encrypt using morse code cipher
encrypted = MorseCodeCipher.encrypt(data)
print(encrypted)

# encrypt using morse code cipher
decrypted = MorseCodeCipher.decrypt(encrypted)
print(decrypted)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)