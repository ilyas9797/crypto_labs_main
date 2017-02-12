from re import sub

with open('decryptAesEcb.txt') as f:
    decrypt_aes_ecb_base64 = sub(r'\n', '', f.read())
f.close()

from binascii import b2a_hex, a2b_base64

decrypt_aes_ecb_str = a2b_base64(decrypt_aes_ecb_base64)

key = b'YELLOW SUBMARINE'

#include pyCrypto
from Crypto.Cipher import AES

#инициализирующий вектор не нужен, так как использутся AES_ECB
cipher = AES.new(key, AES.MODE_ECB)

encrypt_aes_ecb_str = cipher.decrypt(decrypt_aes_ecb_str)

print(encrypt_aes_ecb_str)
print()

s = ''
for i in range(len(encrypt_aes_ecb_str)):
    s += chr(encrypt_aes_ecb_str[i])

print(s)

