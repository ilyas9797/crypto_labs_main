
'''
#производит операцию XOR над исходной строкой s и строкой той же длинны lenght с повторяющимся кодом латинской буквы letter
def text_decryption(s, letter, lenght):
    #создание строки, состоящего из одной повторяющейся len(h) буквы латинского letter
    l = letter
    l = l * lenght
    return lab0_task2.my_xor(s, l)

def relative_freq(texts_array, letter_str, theor_freq_array):
    lenght = len(texts_array[0])
    min = [0]
    freq = 0
    freq_array = []
    #перебор раскодированных строк
    for i in range(len(texts_array)):
        #подсчет количества каждой из букв
        text = str(texts_array[i]).upper()
        for j in range(26):
            #рассматриваемый символ
            sym = lab0_task2.make_hex_line(letter_str[j]).decode('utf-8')
            c = int(text.count(sym))
            #разница между теоретическим значением частоты данной буквы и экспериментальным
            freq += abs((float(c/lenght)) - theor_freq_array[j]/100)
        freq_array.append(freq)
        if (freq < freq_array[min[0]]):
            min.clear()
            min.append(i)
        elif(freq == freq_array[min[0]]):
            min.append(i)
        freq = 0
    return min

def hex_to_str(s):
    strout = ''
    for j in range(int(len(s) / 2)):
        strout += chr(int(s[j * 2:j * 2 + 2:], 16))
    return strout

# применение операции XOR к строке и каждой из букв латинского алфавита
def make_s_XOR_for_all_letters(s, theor_freq_array):
    decrypt_texts_array = []
    # массив кодов всех латинских букв верхнего и нижнего регистра в шестнадцатеричном формате
    letters_str = [hex(65 + i)[2:] for i in range(26)] + [hex(97 + i)[2:] for i in range(26)]

    if(len(s) % 2 != 0):
        s += '0'
    h = lab0_task2.make_hex_line(s)

    for letter in letters_str:
        decrypt_text = text_decryption(s, letter, len(h))
        decrypt_texts_array.append(hex_to_str(decrypt_text))
    min = relative_freq(decrypt_texts_array, letters_str, theor_freq_array)
    str_out = ''
    for i in min:
        str_out += '\n' + decrypt_texts_array[i]
    return str_out
'''

def hex_to_str(s):
    strout = ''
    for j in range(int(len(s) / 2)):
        strout += chr(int(s[j * 2:j * 2 + 2:], 16))
    return strout

def make_one_byte_XOR(enc_str):
    if(len(enc_str) % 2 != 0):
        return None

    from lab0_task2 import  my_xor

    dec_str = ''

    theor_freq_array = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406,
                        6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

    #A-Z: 41h-5ah(65-90)
    #a-z: 61h-7ah(97-122)
    upper_str_list = []
    lower_str_list = []
    for letter in range(65, 91):
        letter_str_up = str(hex(letter)[ 2 : ]) * int(len(enc_str) / 2)
        result_str_up = my_xor(enc_str, letter_str_up)

        letter_str_low = str(hex(letter + 32)[2:]) * int(len(enc_str) / 2)
        result_str_low = my_xor(enc_str, letter_str_low)

        #подсчет числа букв в расшифрованой строке
        #print(letter - 65, ':')
        #alphapet_letters_amount_up = int(len(result_str_up) / 2)
        alphapet_letters_amount_up = int(0)
        result_str_up_only_alphabet = ''
        #print(hex_to_str(result_str_up))
        #alphapet_letters_amount_low  = int(len(result_str_up) / 2)
        alphapet_letters_amount_low = int(0)
        result_str_low_only_alphabet = ''
        #print(hex_to_str(result_str_low))
        #'''
        for i in range(int(len(enc_str) / 2)):
            if ((int(result_str_up[i * 2: i * 2 + 2:], 16) >= 65 and int(result_str_up[i * 2: i * 2 + 2:],
                                                                         16) <= 90) or (
                    int(result_str_up[i * 2: i * 2 + 2:], 16) >= 97 and int(result_str_up[i * 2: i * 2 + 2:],
                                                                            16) <= 122)):
                alphapet_letters_amount_up += 1
                result_str_up_only_alphabet += result_str_up[i * 2: i * 2 + 2:]
            if ((int(result_str_low[i * 2: i * 2 + 2:], 16) >= 65 and int(result_str_low[i * 2: i * 2 + 2:],
                                                                         16) <= 90) or (
                    int(result_str_low[i * 2: i * 2 + 2:], 16) >= 97 and int(result_str_low[i * 2: i * 2 + 2:],
                                                                            16) <= 122)):
                alphapet_letters_amount_low += 1
                result_str_low_only_alphabet += result_str_low[i * 2: i * 2 + 2:]

        #'''

        # сравнение каждого символа строки с выбранной заглавной буквой
        if(int(alphapet_letters_amount_up) != 0):

            delta_up = float(0)


            #выбор буквы из алфавита
            for i_in_alphabet in range(65, 91):
                letter_amount_up = int(0)

                #сравнение каждого символа строки с выбранной буквой
                letter_amount_up = int(str(hex_to_str(result_str_up_only_alphabet)).count(chr(i_in_alphabet))) + int(
                    str(hex_to_str(result_str_up_only_alphabet)).count(chr(i_in_alphabet + 32)))

                delta_up += float(abs(theor_freq_array[i_in_alphabet - 65] / 100 - letter_amount_up / alphapet_letters_amount_up))

            upper_str_list.append([float(delta_up), result_str_up])

        # сравнение каждого символа строки с выбранной прописной буквой
        if(int(alphapet_letters_amount_low) != 0):
            delta_low = float(0)

            # выбор буквы из алфавита
            for i_in_alphabet in range(65, 91):
                letter_amount_low = int(0)

                # сравнение каждого символа строки с выбранной буквой
                letter_amount_low = int(str(hex_to_str(result_str_low_only_alphabet)).count(chr(i_in_alphabet))) + int(
                    str(hex_to_str(result_str_low_only_alphabet)).count(chr(i_in_alphabet + 32)))

                delta_low += float(
                    abs(theor_freq_array[i_in_alphabet - 65] / 100 - letter_amount_low / alphapet_letters_amount_low))

            lower_str_list.append([float(delta_low), result_str_low])

    out_list = []

    if(int(len(upper_str_list)) != 0):
        min_up = int(0)
        for i in range(int(len(upper_str_list))):
            if(upper_str_list[i][0] < upper_str_list[min_up][0]):
                min_up = i
        out_list.append(upper_str_list[min_up])

    if(int(len(lower_str_list)) != 0):
        min_low = int(0)
        for j in range(int(len(lower_str_list))):
            if (lower_str_list[j][0] < lower_str_list[min_low][0]):
                min_low = j
        out_list.append(lower_str_list[min_low])
    return out_list

'''
s = '041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215'
res = make_one_byte_XOR(s)
print()
print()
print(hex_to_str(res[0][1]))
print(hex_to_str(res[1][1]))
'''





