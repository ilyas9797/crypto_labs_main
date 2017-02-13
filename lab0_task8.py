with open('detectEcb.txt') as f:
    file_lines_list = f.read().splitlines()
f.close()

from binascii import a2b_hex


bin_lines_list = [a2b_hex(x) for x in file_lines_list]



import re

list_of_num_encrypt_lines = []

for s in range(len(lines_list) - 1):
    l = len(s)
    num_iters = int(l // 16)
    for i in range(num_iters):
        pattern_line = lines_list[i : i + 16 :]
        p = re.compile(pattern_line)
        m = p.findall(pattern_line)


