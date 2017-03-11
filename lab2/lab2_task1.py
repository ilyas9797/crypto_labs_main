from lab1.lab1_task1_task2 import padding_str, checking_padding
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random.random import randint
from binascii import a2b_base64, b2a_base64

key = None

def first_func_encode_txt():
    with open("lab2_task1_random_strs.txt", "r") as f:
        str_list = f.read().split('\n')
    f.close()

    #128-битный ключ
    global key
    key = Random.new().read(AES.key_size[0])

    iv = b'0' * AES.block_size

    plain_str = str_list[randint(0, len(str_list) - 1)]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    iv_encrypted_str = iv + cipher.encrypt(padding_str(plain_str, AES.block_size))

    return iv_encrypted_str

def second_func_decode_txt(iv_encrypted_str):
    if not key or type(key) != bytes:
        return None

    cipher = AES.new(key, AES.MODE_CBC, iv_encrypted_str[: AES.block_size])

    decrypted_str = cipher.decrypt(iv_encrypted_str[AES.block_size:])

    if not checking_padding(decrypted_str):
        return False
    else:
        return True


#полученные IV с зашифрованной строкой
iv_encrypted_str = first_func_encode_txt()

deciphered_str = b''

#расшифровываем каждый 16-байтный блок, причем, расшифровываемый на каждой итерации блок под индексом i+1
for i in range(len(iv_encrypted_str) // AES.block_size - 1):
    pass

