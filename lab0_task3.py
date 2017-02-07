import lab0_task2

#производит операцию XOR над исходной строкой s и строкой той же длинны lenght с повторяющимся кодом латинской буквы letter
def text_decryption(s, letter, lenght):
    #создание строки, состоящего из одной повторяющейся len(h) буквы латинского letter
    l = letter
    l = l * lenght
    return lab0_task2.my_xor(s, l)

def relative_freq(texts_array, letter_str, theor_freq_array):
    lenght = len(texts_array[0])
    min = 0
    freq = 0
    freq_array = []
    #перебор 52 раскодированных строк
    for i in range(52):
        #подсчет количества каждой из букв
        text = str(texts_array[i]).upper()
        for j in range(26):
            #рассматриваемый символ
            sym = lab0_task2.make_hex_line(letter_str[j]).decode('utf-8')
            c = int(text.count(sym))
            #разница между теоретическим значением частоты данной буквы и экспериментальным
            freq += abs((float(c/lenght)) - theor_freq_array[j]/100)
        freq_array.append(freq)
        if (freq <= freq_array[min]):
            min = i
        freq = 0
    return min


# применение операции XOR к строке и каждой из букв латинского алфавита
def make_s_XOR_for_all_letters(letters_str):
    decrypt_texts_array = []
    for letter in letters_str:
        decrypt_text = text_decryption(s, letter, len(h))
        decrypt_texts_array.append(lab0_task2.make_hex_line(decrypt_text).decode('utf-8'))
        # print(lab0_task2.make_hex_line(letter).decode('utf-8'), lab0_task2.make_hex_line(decrypt_text).decode('utf-8'))
    min = relative_freq(decrypt_texts_array, letters_str, theor_freq_array)
    print(decrypt_texts_array[min])


s = '041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215'
theor_freq_array = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074 ]
h = lab0_task2.make_hex_line(s)


#массив кодов всех латинских букв верхнего и нижнего регистра в шестнадцатеричном формате
letters_str = [hex(65 + i)[2:] for i in range(26)] + [hex(97 + i)[2:] for i in range(26)]






