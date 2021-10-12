<h1 align="center">Decrypto</h1>
<p align="center">A light-weight encryption & decryption library, Built with power and simplicity!</p>
<h2 align="center">
  [![GitHub issues](https://img.shields.io/github/issues/pyGuru123/Decrypto?logo=github)](https://github.com/pyGuru123/Decrypto/issues)
</h2>

<p>
    Decrypto is a light-weight python package to provide state of the art encryption and decryption techniques and aims to be simple and easy to use. Being open-source, Decrypto wraps a huge number of old, modern, secure and encoding based encryption-decryption methods while still being fast<br><br>
</p>

<h2>Features</h2>
<ul>
    <li>It's light-weight and fast</li>
    <li>Simple to use and learn</li>
    <li>Provides a multidegree of techniques from various cryptographic field</li>
</ul>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install decrypto.

```bash
pip install decrypto
```

## Usage

```python
from decrypto import MorseCodeCipher

data = 'Hello World'

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
