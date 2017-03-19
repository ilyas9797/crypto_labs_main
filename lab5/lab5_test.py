from math import sqrt, floor
from binascii import a2b_hex

import hashlib

n = 23454565

b = hex(n)[2:].encode()
b += b'0' if len(b) % 2 != 0 else b''
h = a2b_hex(b)



print(h)

print(type(hashlib.sha1(h)), type(hashlib.sha1(h).hexdigest()))