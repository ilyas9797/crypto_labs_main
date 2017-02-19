from Crypto.Random.random import getrandbits

s = getrandbits(300000)

print(type(s))