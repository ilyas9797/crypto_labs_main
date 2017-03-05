from lab1.lab1_task5 import make_aes_128_ecb
from Crypto import Random
from binascii import a2b_base64, b2a_base64
from lab1.lab1_task1_task2 import padding_str
from Crypto.Cipher import AES
from Crypto.Random.random import randint

unknownStrBase64 = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcy' \
                   'BvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

unknownStr = b2a_base64(unknownStrBase64.encode())

key = Random.new().read(AES.block_size)

random_prefix = Random.new().read(randint(1,20))

decrypted_unknown_str = b''

test_str = random_prefix + b'A' * (AES.block_size - len(random_prefix) % AES.block_size) + b'A' * AES.block_size





for k in range(len(unknownStr)):
    test_str = bytes(test_str[1:]) + chr(unknownStr[k]).encode()

    enc_test_str = make_aes_128_ecb(test_str, key)
    for j in range(256):
        predict_str = test_str[: len(test_str) - 1:] + chr(j).encode()
        enc_predict_str = make_aes_128_ecb(predict_str, key)
        if enc_predict_str == enc_test_str:
            decrypted_unknown_str += chr(predict_str[-1]).encode()
            break

print(a2b_base64(decrypted_unknown_str))

