import binascii
s0 = 'fa'
#s1 = 'faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0'
s1 = 'faea8766efd8b295a633908a3c08'
s2 = s1 + '6d'
s3 = s2 + '7e'

'''tmp_str = (binascii.a2b_hex(s.encode('utf-8'))).decode('utf-8')
num_str = 0
for j in range(3):
    tmp_char_code = ord(tmp_str[j])
    num_str += (tmp_char_code << (2 - j)*8)
bin_str = '0'*(24 - len(bin(num_str)[2:])) + bin(num_str)[2:]
print(bin_str, len(bin_str))'''

'''table_base64 = open('table_base64', 'r')
base64_array = []
for line in table_base64:
    base64_array.append(line[0])
print(base64_array)'''

'''#создание byte-line для строки s
data = s1.encode('utf-8')
if (len(data) %2 != 0):
    data = data + b'0'
import binascii
#преобразование byte-line в шестнадцатеричное представление массива байт
h = binascii.a2b_hex(data)
import base64
#преобразование шестнадцатеричного-представления массива байт в base64-представление
b = base64.b64encode(h)
print('base64:', b.decode('utf-8'))

#преобразование base64-представления в шестандцатеричное представление массива байт
h = base64.b64decode(b)
#преобразование преобразование шестнадцатеричного-представления массива байт в byte-line
data = binascii.b2a_hex(h)
#получение строки из ее представления в виде byte-line
s = data.decode('utf-8')
print('hex-представление:', s)'''

print(hex(int(8)))