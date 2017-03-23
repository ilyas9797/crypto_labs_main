e = 61
C = 2912746968
n = 4369670321
d = 214895317

j = 1
tmp = pow(C, e ** j, n)
while tmp != C:
    j += 1
    tmp = pow(tmp, e, n)

M = pow(C, pow(e, j - 1), n)

print(M)
print(pow(C, d, n))
