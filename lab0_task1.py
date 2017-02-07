#faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0

#создание byte-line для строки s
#data = s.encode('utf-8')
#if (len(data) %2 != 0):
#    data = data + b'0'
#import binascii
#преобразование byte-line в шестнадцатеричное представление массива байт
#h = binascii.a2b_hex(data)
#print(h)
#import base64
#преобразование шестнадцатеричного-представления массива байт в base64-представление
#b = base64.b64encode(h)
#print('base64:', b.decode('utf-8'))

#преобразование base64-представления в шестандцатеричное представление массива байт
#h = base64.b64decode(b)
#преобразование преобразование шестнадцатеричного-представления массива байт в byte-line
#data = binascii.b2a_hex(h)
#получение строки из ее представления в виде byte-line
#s = data.decode('utf-8')
#print('hex-представление:', s)

#вход: hex число записанное в формате строки s
#выход: bin число записанное в формате строки bin_str
def convert_hexstr_in_binstr(s):
    if(len(s) != 6):
        return None
    #переменная, содержащая выходную строку в численном формате
    num_str = 0
    #len(tmp_str)=3
    for j in range(3):
        #переменная, содержащая код jого символа в строке tmp_str
        tmp_char_code = int(s[j * 2:j * 2 + 2:], 16)
        #заполнение num_str с 3его по 1ый байты кодами jых элементов в строке tmp_str
        num_str += (tmp_char_code << (2 - j) * 8)
    #преобразование числа num_str в строку длинны 24, где каждые 8 символов соответствуют двоичному представлению 2 символов hex-представления из строки s
    bin_str = '0' * (24 - len(bin(num_str)[2:])) + bin(num_str)[2:]
    return bin_str

#вход: bin число в строковом формате длинны 24
#выход: строка длинны 4 - power в формате base64 соответствующая входной бинарной строке
def convert_binstr_in_base64str(bin_str, power):
    if(len(bin_str) != 24 ):
        return None
    base64_str = ''
    #создание массива base64_array, содержащего все элементы формата base64, в порядке соответсвующем стандарту base64
    table_base64 = open('table_base64', 'r')
    base64_array = []
    for line in table_base64:
        base64_array.append(line[0])
    table_base64.close()

    #замена всех последующих 6 битов из входной строки на соответсвующий им элемент формата base64
    iter_amount = int(4 - power)
    for i in range(iter_amount):
        #позиция элемента формата base64 в массиве base64_array соответсвующего расматриваемому 6 битному блоку
        pos = int(bin_str[6*i:6*i+6:],2)
        base64_str += base64_array[pos]
    return base64_str



def convert_to_base64(s):
    #длина байтовой строки должна быть четной, т.к. на один байт приходится 2 элемента строки
    if(len(s) % 2 != 0):
        return None
    else:
        out = ''
        #количество блоков длинны 6 в строке s
        iter_amount = int((len(s) / 2) // 3)
        last_iter = int((len(s) / 2) % 3)

        #на каждой итерации преобразуются следующие 6 элементов строки s
        for i in range(iter_amount):
            #преобразование hex числа записанного в формате строки в bin число записанное в формате строки tmp_str
            tmp_str = convert_hexstr_in_binstr(s[i * 6:i * 6 + 6:])
            #преобразование bin числа записанного в формате строки tmp_str в строку в формате base64 длинны 4
            out += convert_binstr_in_base64str(tmp_str, 0)

        #случай если в конце остались 2 необработанных байта
        if(last_iter == 2):
            tmp_str = convert_hexstr_in_binstr(s[(iter_amount - 1) * 6 + 6:] + '0' * 2)
            out += convert_binstr_in_base64str(tmp_str, 1) + '='

        #случай если в конце остались 1 необработанный байт
        elif(last_iter == 1):
            tmp_str = convert_hexstr_in_binstr(s[(iter_amount - 1) * 6 + 6:] + '0' * 4)
            out += convert_binstr_in_base64str(tmp_str, 2) + '=='
        return out

s1 = 'faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0'
s2 = s1 + '6d'
s3 = s2 + '7e'
print('input')
print(s1)
print()
b = convert_to_base64(s1)
print(b)

#обратное преобразование--------------------------------------------------------------------------------------------------------

def convert_base64str_in_binstr(s):
    if (len(s) != 4):
        return None
    bin_str = ''
    # создание словаря base64_dict, содержащего все элементы формата base64, в порядке соответсвующем стандарту base64 и их двоичные коды
    table_base64 = open('table_base64', 'r')
    base64_dict = {}
    for line in table_base64:
        base64_dict[line[0]] = line[1:7:]
    table_base64.close()
    for i in range(4):
        bin_str += base64_dict[s[i]] if s[i] != '=' else '000000'
    return bin_str

def convert_binstr_in_hexstr(bin_str, power):
    if (len(bin_str) != 24):
        return None
    else:
        # замена каждого байта в полученной двоичной строке на hex  аналог
        hex_str = ''
        iter_amount = int(3 - power)
        for i in range(iter_amount):
            hex_str_byte = hex(int(bin_str[8 * i:8 * i + 8:], 2))[2:]
            hex_str_byte = '{0:0>2}'.format(hex_str_byte)
            hex_str += hex_str_byte
        return hex_str


def convert_from_base64(s):
    if(len(s) % 4 != 0):
        return None
    else:
        out = ''
        if(len(s) != 0):
            #количество блоков длинны 4 в строоке s
            iter_amount = int(len(s) / 4)
            # на каждой итерации преобразуются следующие 4 элемента строки s
            for i in range(iter_amount - 1):
                #преобразование блока из 4 элементов формата base64 в двоичную строку длинны 24
                tmp_str = convert_base64str_in_binstr(s[i * 4:i * 4 + 4])
                out += convert_binstr_in_hexstr(tmp_str, 0)
            if(s[(iter_amount - 1) * 4 + 3] != '='):
                tmp_str = convert_base64str_in_binstr(s[(iter_amount - 1) * 4:(iter_amount - 1) * 4 + 4])
                out += convert_binstr_in_hexstr(tmp_str, 0)
            elif(s[(iter_amount - 1) * 4 + 3] == '=' and s[(iter_amount - 1) * 4 + 2] != '='):
                tmp_str = convert_base64str_in_binstr(s[(iter_amount - 1) * 4:(iter_amount - 1) * 4 + 4])
                out += convert_binstr_in_hexstr(tmp_str, 1)
            else:
                tmp_str = convert_base64str_in_binstr(s[(iter_amount - 1) * 4:(iter_amount - 1) * 4 + 4])
                out += convert_binstr_in_hexstr(tmp_str, 2)
    return out

s_out = convert_from_base64(b)
print(s_out)


