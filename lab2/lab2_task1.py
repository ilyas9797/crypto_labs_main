from lab1.lab1_task1_task2 import padding_str, checking_padding
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random.random import randint
from binascii import a2b_base64, b2a_base64

#ключ шифрования
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
    print(plain_str)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    iv_encrypted_str = iv + cipher.encrypt(padding_str(a2b_base64(plain_str), AES.block_size))

    return iv_encrypted_str

#расшифровка сообщений исходным ключем и проверка padding
def second_func_decode_txt(iv_encrypted_str):
    if not key or type(key) != bytes:
        return None
    cipher = AES.new(key, AES.MODE_CBC, iv_encrypted_str[: AES.block_size])

    decrypted_str = cipher.decrypt(iv_encrypted_str[AES.block_size:])

    if decrypted_str[AES.block_size - 2] == b'\x02':
        k = 0
        k += 1

    if not checking_padding(b'\x00' + decrypted_str):
        return False
    else:
        return True


#полученные IV с зашифрованной строкой
iv_encrypted_str = first_func_encode_txt()

#расшифровываемый по ходу работы программы текст
deciphered_str = b''

#расшифровываем каждый 16-байтный блок
for block_num in range(1, len(iv_encrypted_str) // AES.block_size):

    #текущий расшифровываемый блок
    cur_block = iv_encrypted_str[block_num * AES.block_size: (block_num + 1) * AES.block_size]

    #вычисляемое промежуточное состояние(записано в обратном порядке)
    intermediate_state = []

    #выработка блока промежуточного сотояния для текущего расшифровываемого блока
    for i in range(15, -1, -1):

        #рассматриваемый padding
        cur_padding = AES.block_size - i

        #список, в i-ой позиции которого находится значение необходимое для...
        tmp = [0 for l in range(AES.block_size)]

        #заполнение элементов с номером большим i желаемым paddingом
        if len(intermediate_state) != 0:
            for j in range(len(intermediate_state)):
                tmp[AES.block_size - 1 - j] = intermediate_state[j] ^ cur_padding #I[i] ^ P'[i]

        #заполнение элементов с номером меньшим i случайными символами
        tmp[0: i] = bytearray(Random.new().read(i))

        #поиск неизвестного символа на i-ой позиции
        for unk in range(256):
            tmp[i] = unk
            prev_block_mod = b''.join(bytes([x]) for x in tmp)
            if second_func_decode_txt(prev_block_mod + cur_block):
                intermediate_state.append(unk ^ cur_padding)
                break

    #блок шифртекста, предшествующий текущему расшифровываемому блоку
    prev_block = iv_encrypted_str[(block_num - 1) * AES.block_size: block_num * AES.block_size]
    for k in range(AES.block_size):
        deciphered_str += bytes([prev_block[k] ^ intermediate_state[AES.block_size - 1 - k]])

print(checking_padding(deciphered_str).decode())
