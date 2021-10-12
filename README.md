<h1 align="center">Decrypto</h1>
<p align="center">A light-weight encryption & decryption library, Built with power and simplicity!</p>
<p align="center">
  <img src='https://img.shields.io/github/issues/pyGuru123/Decrypto?logo=github&color=blue'>
  <img src='https://img.shields.io/github/stars/pyGuru123/Decrypto?style=social'>
  <img src='https://img.shields.io/github/forks/pyGuru123/Decrypto?style=social&logo=git'>
  <img src='https://img.shields.io/badge/License-MIT-brightgreen'>
  <img src='https://img.shields.io/maintenance/yes/2021'>
</p>

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

cipher = MorseCodeCipher()
data = 'Hello World'

# encrypt using morse code cipher
encrypted = cipher.encrypt(data)
print(encrypted)

# decrypt using morse code cipher
decrypted = cipher.decrypt(encrypted)
print(decrypted)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
