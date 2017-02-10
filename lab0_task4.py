import lab0_task3
# 04,

for file_index in range(1, 18):
    encrypt_file = open('detectSingleXor' + '{0:0>2}'.format(str(file_index)))

    bests_texts_array = []

    # выбираем для каждой строки файла наиболее правдоподобную расшифровку
    for line in encrypt_file:
        string = line[:len(line) - 1]
        file_str_list = lab0_task3.make_one_byte_XOR(string)
        for i in range(int(len(file_str_list))):
            bests_texts_array.append(file_str_list[i])

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
        print('   ' + lab0_task3.hex_to_str(bests_texts_array[min_str[i]][1]))


