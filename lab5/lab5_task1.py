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

def sqrt1(x):
    s = round(x ** 0.5)
    return (x - s ** 2) // (2 * s) + s



#17 вариант
e = 823
n = 850706101864879069718554963638566789
P = 0x70f61ca1b5bdc42b4fd984092d2b8f593589cb2e
Q = 0x9a1874da77f7c80b16513c523ff6564ace49bebd
D = 0xa206a8c8427c0968f2b3336aac73e1192d35c0f1

#метод Ферма
x_min = sqrt1(n) + 1

tmp = x_min ** 2 - n

p, q = 0, 0

for x in range(n - (x_min - 1)):
    sqrt_tmp = sqrt(tmp)
    tmp = tmp + 2 * (x_min + x) + 1
    if sqrt_tmp - floor(sqrt_tmp) == 0:
        #x (+/-) sqrt(x^2 - n)
        p = x_min + x + floor(sqrt_tmp)
        q = x_min + x - floor(sqrt_tmp)
        break

euler_n = (p - 1) * (q - 1)
ext_euclid_tuple = gcdex(e, euler_n)
d = ext_euclid_tuple[1] % euler_n

print(p, q, d, p*q)
print(sha1(str(d).encode()).hexdigest())




