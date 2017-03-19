from math import sqrt, floor
from hashlib import sha1
from binascii import a2b_hex

#расширенная теорема Евклида
def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)

#17 вариант
e = 823
n = 850706101864879069718554963638566789
P = 0x70f61ca1b5bdc42b4fd984092d2b8f593589cb2e
Q = 0x9a1874da77f7c80b16513c523ff6564ace49bebd
D = 0xa206a8c8427c0968f2b3336aac73e1192d35c0f1

#метод Ферма
x_min = floor(sqrt(n)) + 1

tmp = x_min ** 2 - n

for x in range(n + 1 - x_min):
    sqrt_tmp = sqrt(tmp)
    tmp = tmp + 2 * (x_min + x) + 1
    if sqrt_tmp - floor(sqrt_tmp) == 0:
        #x (+/-) sqrt(x^2 - n)
        p = x_min + x + floor(sqrt_tmp)
        q = x_min + x - floor(sqrt_tmp)
        #если  p и q не тривиальны
        if p != 1 and q != 1:
            euler_n = (p - 1) * (q - 1)
            ext_euclid_tuple = gcdex(e, euler_n)
            #если найденное euler_n взаимно простое с выбранным e
            if ext_euclid_tuple[0] == 1:
                d = ext_euclid_tuple[1]
                d = d % euler_n
                #бинарное представление d для функции sha1
                bin_d = hex(d)[2:].encode()
                bin_d += b'0' if len(bin_d) % 2 != 0 else b''
                bin_d = a2b_hex(bin_d)

                if sha1(bin_d).hexdigest() == str(D)[2:]:
                    break







