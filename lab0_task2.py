#вход: строка s содержащая коды символов в шестандцатеричном формате
#выход: бинарная строка h содержащая символы соответствующие их кодам в строке s
def make_hex_line(s):
    # создание byte-line для строки s
    #data = s.encode('utf-8')
    #s = bytes(s, 'utf-8')
    if (len(s) % 2 != 0):
        s = s + '0'
    import binascii
    # преобразование byte-line в шестнадцатеричное представление массива байт
    h = binascii.a2b_hex(s)
    return h

#вход: бинарная строка h содержащая символы из ASCII
#выход: строка s содержащая коды символов в шестандцатеричном формате соответствующие символам из строки h
def make_str_line(h):
    import binascii
    # преобразование преобразование шестнадцатеричного-представления массива байт в byte-line
    data = binascii.b2a_hex(h)
    # получение строки из ее представления в виде byte-line
    s = data.decode('utf-8')
    return s

#вход: строки s1 и s2 содержащие коды символов в шеснадцатеричном формате
#выход: строка outs содержащие коды проXORенных символов из s1 и s2 в шеснадцатеричном формате
def my_xor(s1, s2):
    if (len(s1) != len(s2)):
        print('Ошибка: длинны массивов не совпадают')
        return None
    else:
        h1 = make_hex_line(s1)
        h2 = make_hex_line(s2)
        i = 0
        h = []
        while i < len(h1):
            h.append(h1[i]^h2[i])
            i+=1
        h = bytes(h)
        outs = make_str_line(h)
        return outs

'''
#8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69
#bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166
#305051cc9a7cc1aa8576dd97ce4ab4ac876af5970b7d62c53d495985e60a929bfd739ded2d65cb0f
s1 = input()
s2 = input()
print(my_xor(s1, s2))
'''