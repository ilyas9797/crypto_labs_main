from math import floor
from hashlib import sha1


def cont_fraction_coeffics(x):
    a_n = floor(x)

    yield a_n

    x_n = x - a_n
    # условие, достижения конца непрерывной дроби
    while x_n != 0:

        a_n = floor(1 / x_n)

        yield a_n

        x_n = 1 / x_n - a_n


def rational_approx_coeffics(x):
    prev_prev_p = 1
    prev_prev_q = 0

    fract_coef_gen = cont_fraction_coeffics(x)

    prev_p = fract_coef_gen.__next__()
    prev_q = 1

    for a in fract_coef_gen:

        p = a * prev_p + prev_prev_p
        q = a * prev_q + prev_prev_q

        yield p, q

        prev_prev_p, prev_prev_q = prev_p, prev_q
        prev_p, prev_q = p, q


def search_ration_approx(e, n, m):
    for p, q in rational_approx_coeffics(e / n):
        if m == pow(m, e * q, n):
            return p, q


e = 12279682238031147226460402005664030881
n = 75847237140497715121748216702036029141
D = 0x50e929700fabf72255b08a79c74a6d330312404f
m = 123

k, d = search_ration_approx(e, n, m)
print(k, d)

print(sha1(str(d).encode()).hexdigest())

euler_n = ((e * d) - 1) // k
print(euler_n)
