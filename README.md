<h1 align="center">Decrypto</h1>
<p align="center">A light-weight encryption & decryption library, Built with power and simplicity!</p>
<p align="center">
  <img src='https://img.shields.io/github/issues/pyGuru123/Decrypto?logo=github&color=blue'>
  <img src='https://img.shields.io/github/stars/pyGuru123/Decrypto?style=social'>
  <img src='https://img.shields.io/github/forks/pyGuru123/Decrypto?style=social&logo=git'>
  <img src='https://img.shields.io/badge/License-MIT-brightgreen'>
  <img src='https://img.shields.io/maintenance/yes/2023'>
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

You can either use a classical cipher technique

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

or a more advanced and modern cipher technique

```python
from decrypto import RSACipher

cipher = RSACipher()
data = 'hello world'

keys = cipher.generate_keys(23, 31)
encrypted = cipher.encrypt(message, keys['public_key'])
decrypted = cipher.decrypt(encrypted, keys['private_key'])

print(keys)
print(encrypted)
print(decrypted)
```

# 

<div align="center">
<img src="https://hacktoberfest.com/_next/static/media/logo-hacktoberfest--horizontal.ebc5fdc8.svg"/> <br/>
This Repository is Participating in Hacktoberfest 2023 <br/><br/>
<img src='https://img.shields.io/github/issues/pyGuru123/Decrypto?logo=github&color=blue'>
<img src='https://img.shields.io/github/stars/pyGuru123/Decrypto?style=social'>
<img src='https://img.shields.io/github/forks/pyGuru123/Decrypto?style=social&logo=git'>
<br/><br/>
</div>

To participate and contribute checkout our issues section. You can also discuss new ideas in our telegram group here [@pyguru](https://t.me/pyguruDiscussion)

Our other repositiores partcipating in Hacktoberfest 2023

* [LLM-Apps](https://github.com/pyGuru123/LLM-Apps)
* [Decrypto](https://github.com/pyGuru123/Decrypto)
* [TG-Api](https://github.com/pyGuru123/tg-api)

