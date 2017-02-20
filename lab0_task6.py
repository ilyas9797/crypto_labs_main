import binascii
import  re

import lab0_task3

file = open('breakRepeatedKeyXor.txt')
str_from_file = str(file.read())
str_from_file2 = ''
file.close()

str_from_file = re.sub('\\n', '', str_from_file)

str_from_file_hex = binascii.a2b_base64(str_from_file)

str_from_file = ''
for i in str_from_file_hex:
    str_from_file += chr(i)

str_from_file_len = int(len(str_from_file))

#(n mod k) = i
#key_list содержит 39 элементов
key_list = []
decrypt_list = []

#перебираем различные длины ключа
for k in range(2, 41):

    #k_key_list содержит k строк для каждой длинны ключа k
    k_key_list = []

    #составление строк, удовлетворяющих условию (n mod k) = i
    for i in range(k):
        i_str = ''

        for n in range(str_from_file_len):
            if(n % k == i):
                i_str += str(str_from_file[n])

        s = binascii.b2a_hex(i_str.encode())
        k_key_list.append(s.decode())

    str_for_k_list = []
    for j in range(len(k_key_list)):
        o = lab0_task3.make_one_byte_XOR(k_key_list[j])
        xored_str = o[len(o) - 1][1]
        xored_str_bin = binascii.a2b_hex(xored_str)
        xored_str = ''
        for m in xored_str_bin:
            xored_str += chr(m)
        str_for_k_list.append(xored_str)

    str_for_k = ''
    j = 0
    for n in range(str_from_file_len):
        if (n % k == 0 and n != 0):
            j += 1
        str_for_k += str_for_k_list[n % k][j]

    print(str(k) + ':')
    print()
    print(str_for_k)
    print()








