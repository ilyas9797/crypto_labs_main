from lab1.lab1_task1_task2 import padding_str, checking_padding
from lab1.lab1_task3 import modifying_encrypted_str, decrypting_and_searching_repl
from Crypto import Random
from Crypto.Random.random import randint
from Crypto.Cipher import AES

def encryption_oracle(input_str):
    if type(input_str) != bytes:
        return None
    #создание 128-битного ключа
    key = Random.new().read(AES.key_size[0])
    print('key=', key)
    iv = b'\x00' * AES.block_size

    #выбор режима шифрования случайным образом
    random_mode = randint(1, 100)
    if random_mode % 2 == 0:
        mode = AES.MODE_ECB
        print('AES.MODE_ECB')
    else:
        mode = AES.MODE_CBC
        print('AES.MODE_CBC')
    cipher = AES.new(key, mode, iv)

    #создание случайной строки случайной длинны
    random_lenght = randint(5, 10)
    random_str = Random.new().read(random_lenght)
    plain_text = padding_str(random_str + input_str + random_str, AES.block_size)

    if cipher.mode == AES.MODE_ECB:
        encrypted_text = cipher.encrypt(plain_text)
    else:
        encrypted_text = iv + cipher.encrypt(plain_text)
    return cipher.mode, plain_text , encrypted_text, cipher




m, plain_text, unknown_mode_encrypted_str, cipher = encryption_oracle(b'tested_string')
if len(unknown_mode_encrypted_str) > 16:
    test_change = Random.new().read(AES.block_size)
    enc_modified = modifying_encrypted_str(plain_text, unknown_mode_encrypted_str, test_change, 0)
    dec = decrypting_and_searching_repl(unknown_mode_encrypted_str, enc_modified, test_change, 0, cipher)
    if dec != None:
        print('detected CBC')
    else:
        print('detected ECB')
else:
    print('detected ECB')