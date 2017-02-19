from Crypto import Random
from Crypto.Cipher import AES
from lab1.lab1_task1_task2 import padding_str, checking_padding
import re

#вход: три байт-строки
#выход: байт-строка, полученная в результате соединения входных строк в соответсвующем порядке(причем, из средней удалены символы ; и =
def padding_begin_and_end(input_str, begin_str, end_str):

    if type(input_str) == bytes and type(begin_str) == bytes and type(end_str) == bytes:

        if len(input_str) != 0 and len(begin_str) != 0 and len(end_str) != 0:

            s = ''
            for k in range(len(input_str)):
                s += chr(input_str[k])
            s_sub = re.sub(r'[\=;]', '', s)

            return begin_str + s_sub.encode() + end_str

#вход: исходная, зашифрованная, желаемая байт-строки и смещение относительно исходной строки, где мы хотим увидеть желаемую подстроку
#выход: зашифрованная байт-строка модифицированная таким образом, что при ее расшифровке мы обнаружим желаемую подстроку
def modifying_encrypted_str(plain_str, enc_str, repl_str, shift):

    if type(plain_str) == bytes and type(enc_str) == bytes and type(repl_str) == bytes:

        if len(plain_str) > len(repl_str) + shift:

            enc_modified = bytearray(enc_str)
            for i in range(len(repl_str)):
                enc_modified[i + shift] = enc_modified[i + shift] ^ plain_str[i + shift] ^ repl_str[i]

            return bytes(enc_modified)

#вход: зашифрованная, модифицированная, желаемая байт-строки, смещение, и AES-объект
#выход: расшифрованная байт-строка с желаемой подстрокой, записанной с позиции равной смещению
def decrypting_and_searching_repl(enc_str, enc_modified_str, repl_str, shift, cipher):

    if type(enc_str) == bytes and type(enc_modified_str) == bytes and type(repl_str) == bytes:

        dec_str = b''

        for j in range(1, int(len(enc_str) / AES.block_size)):
            enc_tmp = enc_modified_str[(j - 1) * AES.block_size: j * AES.block_size:] + enc_str[j * AES.block_size: (
                                                                                                            j + 1) * AES.block_size:]
            dec_str += cipher.decrypt(enc_tmp)[AES.block_size: 2 * AES.block_size:]

        if dec_str[shift: shift + len(repl_str):] == repl_str:
            return dec_str

'''
begin_str = b'comment1=cooking%20MCs;userdata='
end_str = b';comment2=%20like%20a%20pound%20of%20bacon'

print('Enter string:')
while True:
    s = str(input())
    if len(s) != 0:
        break
    print('Enter string again:')

str_to_encrypt = padding_begin_and_end(s.encode(),begin_str,end_str)

#случайная генерация ключа
key = Random.new().read(AES.key_size[0])
print('key = ', key)

#инициализирующий вектор заполненный нулями
iv = b'\x00' * AES.block_size

cipher = AES.new(key, AES.MODE_CBC, iv)

#заполнение исходной строки по стандарту PKCS7
p_s = padding_str(str_to_encrypt, AES.block_size)

enc = iv + cipher.encrypt(p_s)

wanted_text = b'admin=true'

shift = 0

enc_modified = modifying_encrypted_str(str_to_encrypt, enc, wanted_text, shift)

dec = decrypting_and_searching_repl(enc, enc_modified, wanted_text, shift, cipher)
if dec != None:
    print(checking_padding(dec))
'''





'''
#случайная генерация ключа
key = Random.new().read(AES.key_size[0])
print('key = ', key)

#инициализирующий вектор заполненный нулями
iv = b'\x00' * AES.block_size

cipher = AES.new(key, AES.MODE_CBC, iv)
''
s_to_encrypt = b'Attack at dawn'

#дополняем исходную строку так, чтобы она состояла из блоков длинны 16, по стандарту PKCS7
ps = padding_str(s_to_encrypt, AES.block_size)

#шифруем исходную строку по алгоритму AES_128_CBC, затем добавляем в начало инициализирующий вектор, это и будет шифртекстом
encrypted = iv + cipher.encrypt(ps)
print(encrypted)
#расшифровываем шифртекст, откидываем первые 16 символов и восстанавливаем исхоную строку, по стандарту PKCS7
decrypted = cipher.decrypt(encrypted)
print(checking_padding(decrypted[16: ]))
''
s_begin = b'comment1=cooking%20MCs;userdata='
s_end = b';comment2=%20like%20a%20pound%20of%20bacon'
print(len(s_begin + s_end))

import re


while True:
    s = input()
    s = re.sub(r'[\=;]', '', s)
    if(len(s) != 0):
        break
    print('Enter string again')

s_to_encrypt = s_begin + s.encode() + s_end

p_s = padding_str(s_to_encrypt, AES.block_size)

enc = iv + cipher.encrypt(p_s)

enc_modified = bytearray(enc)

#A xor B xor C xor sym = sym, where A = decode(C[N]), B = C[N-1], C - original text
wanted_text = b'admin=true'

#shift < 65
shift = 64

for i in range(len(wanted_text)):
    #
    enc_modified[i + shift] = enc_modified[i + shift] ^ s_to_encrypt[i + shift] ^ wanted_text[i]

''
decrypted = cipher.decrypt(bytes(encrypted))
print(checking_padding(decrypted[16: ]))
''

enc_modified = bytes(enc_modified)

dec = b''

for j in range(1, int(len(enc) / AES.block_size)):
    enc_tmp = enc_modified[(j - 1) * AES.block_size: j * AES.block_size:] + enc[j * AES.block_size: (j + 1) * AES.block_size]
    dec += cipher.decrypt(enc_tmp)[AES.block_size: 2 * AES.block_size: ]

print(checking_padding(dec))

string_dec = ''
for k in range(len(dec)):
    string_dec += chr(dec[k])

p = re.compile(wanted_text.decode())
print(p.search(string_dec))
'''
