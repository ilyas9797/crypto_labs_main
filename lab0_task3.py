#перевод бинарной строки в обычную
def hex_to_str(s):
    strout = ''
    for j in range(int(len(s) / 2)):
        strout += chr(int(s[j * 2:j * 2 + 2:], 16))
    return strout

#вход: строка, содержащая hex-предствление зашифрованной строки
#выход: список пар значений наиболее вероятных строк, где первый элемент дельта между средним и текущем распределениями букв
def make_one_byte_XOR(enc_str):
    if(len(enc_str) % 2 != 0):
        return None

    from lab0_task2 import  my_xor

    theor_freq_array = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406,
                        6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

    #возвращаемая переменная, мы можем быть уверены, что значение дельты будет меньше 10 процентов
    min_list = [[float(100), '']]

    #перебор всевозможных символов, с помощью которых мы пытаемся расшифровать входную строку
    for letter in range(256):
        #строка длинны равной зашифрованной строке, содержащая hex-представление одной повторяющейся буквы
        letter_str = '{0:0>2}'.format(str(hex(letter)[ 2 : ])) * int(len(enc_str) / 2)
        #результат xor зашифрованной строки с строкой одного байта
        result_str = my_xor(enc_str, letter_str)

        alphapet_letters_amount = int(0)
        result_str_only_alphabet = ''

        import re
        #преобразование шестнадцатеричного представления проXORенной строки в строку, для того чтобы отфильтровать ее, оставив только латинские символы
        result_str_str = hex_to_str(result_str)

        p = re.compile('[A-Za-z]+')
        m = p.findall(result_str_str)

        #удаление не латинских символов
        for i in range(int(len(m))):
            alphapet_letters_amount += int(len(m[i]))
            result_str_only_alphabet += str(m[i])

        # сравнение каждого символа строки с выбранной буквой
        if (int(alphapet_letters_amount) != 0):

            delta = float(0)

            # выбор буквы из алфавита и определение самой вероятной строки(чем меньше дельта, тем вероятнее)
            for i_in_alphabet in range(65, 91):
                # сравнение каждого символа строки с выбранной буквой
                p = re.compile('[' + chr(i_in_alphabet) + chr(i_in_alphabet + 32) + ']')
                letter_amount_up = int(len(p.findall(result_str_only_alphabet)))

                delta += float(
                    abs(theor_freq_array[i_in_alphabet - 65] / 100 - letter_amount_up / alphapet_letters_amount))

            if (delta < min_list[0][0]):
                min_list.clear()
                min_list.append([float(delta), result_str])

            elif(delta == min_list[0][0]):
                min_list.append([float(delta), result_str])


    return min_list

'''
s = '041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215'
res = make_one_byte_XOR(s)
print()
print()
print(res[0][1])
print(res[1][1])
'''





