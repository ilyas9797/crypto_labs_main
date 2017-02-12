s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

l = int(len(s))

k = int(5)

e = ''

for i in range(k):
    e_i = ''
    for n in range(l):
        if(n % k == i):
            e_i += s[n]
    e += e_i

print(e)


d = [0 for i in range(l)]

if(l % k == 0):
    for j in range(l):
        i = j // (l // k)
        j1 = j % (l // k)
        d[j1 * k + i] = e[j]
else:
    c = (l % k) * (l // k + 1)
    for j in range(l):
        if(j < c):
            i = j // (l // k + 1)
            j1 = j % (l // k + 1)
            d[j1 * k + i] = e[j]
        else:
            i = (j - c) // (l // k) + (l % k)
            j1 = (j - c) % (l // k)
            d[j1 * k + i] = e[j]

print(d)


