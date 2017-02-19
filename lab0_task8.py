with open('detectEcb.txt') as f:
    file_lines_list = f.read().splitlines()
f.close()

from binascii import a2b_hex

bin_lines_list = [a2b_hex(x) for x in file_lines_list]

lines_list = []

for i in range(len(bin_lines_list) - 1):
    lines_list.append('')
    for j in range(len(bin_lines_list[i])):
        lines_list[i] += chr(bin_lines_list[i][j])

for k in lines_list:
    list_i_matchings = []
    for n in range(len(k) - 16):
        s_n = k[ n : n + 16 : ]
        found_start_index = str(k).find(s_n, n + 16)
        if found_start_index != -1:
            if len(list_i_matchings) == 0:
                list_i_matchings.append(n)
            list_i_matchings.append(found_start_index)

    if len(list_i_matchings) != 0:
        print('Line: ', str(lines_list.index(k)))
        print(' Matching substring: ')
        print('---------------------')
        print('     Byte line:')
        print('---------------------')
        print(str(k[list_i_matchings[0]: list_i_matchings[0] + 16: ]).encode())
        print('---------------------')
        print('     String:')
        print('---------------------')
        print(str(k[list_i_matchings[0]: list_i_matchings[0] + 16: ]))
        print('---------------------')
        for m in list_i_matchings:
            print('(' + str(m) + ', ' + str(m + 16) + ')')



