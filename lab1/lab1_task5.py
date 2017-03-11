from lab1.lab1_task1_task2 import padding_str
from binascii import b2a_base64, a2b_base64
from Crypto.Cipher import AES
from Crypto import Random

def make_aes_128_ecb(plain_text, key):

    cipher = AES.new(key, AES.MODE_ECB)

    return cipher.encrypt(plain_text)


'''
unknownStrBase64 = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcy' \
                   'BvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

unknownStr = b2a_base64(unknownStrBase64.encode())

key = Random.new().read(AES.block_size)

test_str = b'A' * AES.block_size

decrypted_unknown_str = b''

for i in range(len(unknownStr)):
    test_str = bytes(test_str[1:]) + chr(unknownStr[i]).encode()
    enc_test_str = make_aes_128_ecb(test_str, key)
    for j in range(256):
        predict_str = test_str[: len(test_str) - 1:] + chr(j).encode()
        enc_predict_str = make_aes_128_ecb(predict_str, key)
        if enc_predict_str == enc_test_str:
            decrypted_unknown_str += chr(predict_str[-1]).encode()
            break

print(a2b_base64(decrypted_unknown_str))
'''