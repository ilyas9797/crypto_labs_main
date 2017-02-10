import lab0_task2

print('Строка:')
in_str = str(input())
print('Ключ:')
key_str = str(input())

l_str = len(in_str)
l_key = len(key_str)

div = int(l_str // l_key)
mod = int(l_str % l_key)

key = ''

for i in range(div):
    key += key_str

key += key_str[ 0 : mod : ]

print('Ключ:')
print(key)

import binascii
in_str_hex = binascii.b2a_hex(in_str.encode()).decode()
key_hex = binascii.b2a_hex(key.encode()).decode()

result_hex = lab0_task2.my_xor(in_str_hex, key_hex)

print(result_hex)