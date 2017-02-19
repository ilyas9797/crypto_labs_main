from lab1.lab1_task1_task2 import padding_str, checking_padding
from Crypto import Random
from Crypto.Random.random import randint
from Crypto.Cipher import AES

def encryption_oracle(input_str):
    if type(input_str) != bytes:
        return None
    key = Random.new().read(AES.key_size[0])
    iv = b'\x00' * AES.block_size

    random_mode = randint(1, 100)
    if random_mode % 2 == 0:
        mode = AES.MODE_ECB
    else:
        mode = AES.MODE_CBC
    cipher = AES.new(key, mode, iv)

    random_lenght = randint(5, 10)
    random_str = Random.new().read(random_lenght)
    plain_text = padding_str(random_str + input_str + random_str, AES.block_size)

    if cipher.mode == AES.MODE_ECB:
        encrypted_text = cipher.encrypt(plain_text)
    else:
        encrypted_text = iv + cipher.encrypt(plain_text)
    return encrypted_text




encryption_oracle(b'tested_string')