import lab0_task3
from binascii import a2b_hex

#поиск зашифрованной строки в каждом файле
for file_index in range(1, 18):
    encrypt_file = open('detectSingleXor' + '{0:0>2}'.format(str(file_index)))

    #список содержащий наиболее вероятную расшифровку для каждой строки в файле
    bests_texts_array = []

    # выбираем для каждой строки файла наиболее правдоподобную расшифровку
    for line in encrypt_file:
        string = line[:len(line) - 1]
        file_str_list = lab0_task3.make_one_byte_XOR(string)
        for i in range(int(len(file_str_list))):
            bests_texts_array.append(file_str_list[i])

    #список с индексами массива bests_texts_array, у которых наименьшая дельта
    min_str = [0]
    for i in range(int(len(bests_texts_array))):
        if(float(bests_texts_array[i][0]) < float(bests_texts_array[min_str[0]][0])):
            min_str.clear()
            min_str.append(i)
        elif(float(bests_texts_array[i][0]) == float(bests_texts_array[min_str[0]][0])):
            min_str.append(i)


    print()
    print('detectSingleXor' + '{0:0>2}'.format(str(file_index)) + ':')
    print(' Right:')
    for i in range(int(len(min_str))):
        print(a2b_hex(str(bests_texts_array[min_str[i]][1]).encode()))


