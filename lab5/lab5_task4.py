from math import sqrt

n = 328583408843

p = 2
while (n % p) != 0:
    p += 1

print(p, n // p, p * (n // p))

