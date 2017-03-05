from math import sqrt, floor

e = 823
n = 850706101864879069718554963638566789

x_min = floor(sqrt(n)) + 1

for x in range(x_min, n + 1):
    sqrt_tmp = sqrt(x ** 2 - n)
    if sqrt_tmp - floor(sqrt_tmp) == 0:
        p = x - sqrt_tmp
        q = x + sqrt_tmp
        if n == p * q and p != 1 and q != 1:
            euler_n = (p - 1) * (q - 1)



