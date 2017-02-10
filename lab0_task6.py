file = open('breakRepeatedKeyXor.txt')
str_from_file = ''
for line in file:
    str_from_file += line[ : len(line) - 1 : ]

str_from_file_len = len(str_from_file)

#(n mod k) = i
key_list = []
for k in range(2, 41):
    k_key_list = []
    for i in range(k):
        i_str = ''
        for n in range(str_from_file_len):
            if(n % k == i):
                i_str += str_from_file(n)
        k_key_list.append(i_str)
    key_list.append(k_key_list)
