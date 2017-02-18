from Crypto import Random
from Crypto.Cipher import AES
from lab1.lab1_task1_task2 import padding_str, checking_padding

#случайная генерация ключа
key = Random.new().read(AES.key_size[0])
print('key = ', key)

#инициализирующий вектор заполненный нулями
iv = b'\x00' * AES.block_size

cipher = AES.new(key, AES.MODE_CBC, iv)
'''
s_to_encrypt = b'Attack at dawn'

#дополняем исходную строку так, чтобы она состояла из блоков длинны 16, по стандарту PKCS7
ps = padding_str(s_to_encrypt, AES.block_size)

#шифруем исходную строку по алгоритму AES_128_CBC, затем добавляем в начало инициализирующий вектор, это и будет шифртекстом
encrypted = iv + cipher.encrypt(ps)
print(encrypted)
#расшифровываем шифртекст, откидываем первые 16 символов и восстанавливаем исхоную строку, по стандарту PKCS7
decrypted = cipher.decrypt(encrypted)
print(checking_padding(decrypted[16: ]))
'''
s_begin = b'comment1=cooking%20MCs;userdata='
s_end = b';comment2=%20like%20a%20pound%20of%20bacon'

from re import sub

while True:
    s = input()
    s = sub(r'[\=;]', '', s)
    if(len(s) != 0):
        break
    print('Enter string again')

s_to_encrypt = s_begin + s.encode() + s_end

p_s = padding_str(s_to_encrypt, AES.block_size)

enc = iv + cipher.encrypt(p_s)

enc_modified = bytearray(enc)

#A xor B xor C xor sym = sym, where A = decode(C[N]), B = C[N-1], C - original text
wanted_text = b'admin=true'
for i in range(len(wanted_text)):
    #
    enc_modified[i + 7] = enc_modified[i + 7] ^ s_to_encrypt[i + 7] ^ wanted_text[i]

'''
decrypted = cipher.decrypt(bytes(encrypted))
print(checking_padding(decrypted[16: ]))
'''

enc_modified = bytes(enc_modified)

for j in range(int(len(enc) / AES.block_size)):
    enc_tmp =
