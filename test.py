'''
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
'''
'''
class Fibonacci:
#Итератор последовательности Фибоначчи до N"""
    def __init__(self, N):
        self.n, self.a, self.b, self.max = 0, 0, 1, N

    def __iter__(self):
    # сами себе итератор: в классе есть метод next()
        return self
    def next(self):
        if self.n < self.max:
            a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b
            return a
        else:
            raise StopIteration
# Использование:
for i in Fibonacci(100):
  print(i)
'''
'''
l = [1234567890, 7654421496, 42325267213, 9823412461, 11222277422346, 73453282345, 9937651836, 42, 666222115293, 8211111143445]

n = int(0)

for i in range(len(l)):
    for j in range(i, len(l)):
        if(i != j):
            if((l[i] < l[j] or l[i] > l[j]) and ((l[i] + l[j]) % 3 == 0)):
                n += 1
print(n)
'''
'''
stack = []

s = input()

error_marker = False

for i in s:
    if i == '(' or i == ')':
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or '(' != stack.pop():
                error_marker = True
                break
    elif i == '[' or i == ']':
        if i == '[':
            stack.append(i)
        else:
            if len(stack) == 0 or '[' != stack.pop():
                error_marker = True
                break
    elif i == '{' or i == '}':
        if i == '{':
            stack.append(i)
        else:
            if len(stack) == 0 or '{' != stack.pop():
                error_marker = True
                break
    else:
        if i == '<':
            stack.append(i)
        else:
            if len(stack) == 0 or '<' != stack.pop():
                error_marker = True
                break
if error_marker == True or len(stack) != 0:
    print('NO')
else:
    print('YES')
'''


