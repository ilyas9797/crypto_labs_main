from re import sub

with open('decryptAesEcb.txt') as f:#/home/ilyas/PycharmProjects/labs/lab0/decryptAesEcb.txt
    decrypt_aes_ecb_base64 = sub(r'\n', '', f.read())
f.close()

from binascii import a2b_base64

decrypt_aes_ecb_str = a2b_base64(decrypt_aes_ecb_base64)

with open('encrypted.txt', 'wb') as f1:
    f1.write(decrypt_aes_ecb_str)
f1.close()

password = b'YELLOW SUBMARINE'
with open('password.txt', 'wb') as f2:
    f2.write(password)
f2.close()

#openssl enc -d -aes-128-ecb -salt -in encrypted.txt -out decrypted.txt -pass file:password.txt
import subprocess
subprocess.call(['openssl', 'enc', '-d', '-aes-128-ecb', '-salt', '-in', 'encrypted.txt', '-out', 'decrypted.txt', '-pass', 'file:password.txt'])


