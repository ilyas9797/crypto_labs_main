from math import sqrt, floor
import lab5.Lab5_hash as lab5_hash

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

for x in range(x_min, n + 1):
    sqrt_tmp = sqrt(x ** 2 - n)
    if sqrt_tmp - floor(sqrt_tmp) == 0:
        #x (+/-) sqrt(x^2 - n)
        p = x - floor(sqrt_tmp)
        q = x + floor(sqrt_tmp)
        sha_p = lab5_hash.sha1(p)
        #если n разлагается на произведение p и q и они не тривиальны
        if n == p * q and p != 1 and q != 1:
            euler_n = (p - 1) * (q - 1)
            ext_euclid_tuple = gcdex(e, euler_n)
            #если найденное euler_n взаимно простое с выбранным e
            if ext_euclid_tuple[0] == 1:
                d = ext_euclid_tuple[1]
                d1 = ext_euclid_tuple[2]







