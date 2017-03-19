from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import a2b_base64

unknown_str = a2b_base64('Or6kII/NM5bDyWwvTGC3B6KFCPz9H2Cxvakxs/uGFmENxPykZx4XJqb62VPGj6rj7w=='.encode())

ctr = Counter.new(64, prefix=b'\x00'*8, initial_value=0, little_endian=True)

key = b'YELLOW SUBMARINE'

cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

decrypted_str = cipher.decrypt(unknown_str).decode()

print(decrypted_str)
