import re
import json
import random
import string
from lab1.lab1_task1_task2 import padding_str, checking_padding
from Crypto.Cipher import AES
from Crypto import Random

def right_email(s):
    #регулярное выражение, проверяющее е-мейл на наличие недопустимых символов
    p = re.compile('[a-zA-Z]+'              #логин начинается с буквы
                   '([-_.]?[a-zA-Z0-9]+)*'  #не более одного особого символа, после которого должна следовать хотя бы одна буква или цифра
                   '@'
                   '[a-zA-Z]+'              #в доменном имени 2-го уровня только латинские символы
                   '[.]'
                   '[a-zA-Z]+')             #в доменном имени 1-го уровня только латинские смиволы
    m = p.match(s)
    if m == None or len(s) > m.end():
        return False
    return True

def parse_to_json(s):
    if len(s) == 0:
        return None
    json_obj = {}
    splitted_list = str(s).split('&')
    for i in splitted_list:
        json_obj[i[0: i.find('=')]] = i[i.find('=') + 1: len(i)]
    return json.dumps(json_obj, indent=4)

def profile_for(email):
    if right_email(email):
        items_list = ['email=',
                      '&uid=',
                      '&strangestr=',
                      '&SN=',
                      '&role=']
        value_list = []

        #длинна uid должна быть такой, чтобы значение поля strangestr начиналось с индекса кратного AES.block_size=16
        tmp_lenght = 0
        for i in range(3):
            tmp_lenght += len(items_list[i])
        uid_lenght = AES.block_size - (tmp_lenght + len(email)) % AES.block_size
        uid = ''.join(random.choice(string.digits) for x in range(uid_lenght))

        #длинна значения поля strangestr должна быть кратна AES.block_size=16
        strangestr = ''.join(chr(x) for x in padding_str(email[: str(email).find('@')], AES.block_size))

        #длинна SN должна быть такой, чтобы значение поля role начиналось с индекса кратного AES.block_size=16
        tmp_lenght = 0
        for s in items_list:
            tmp_lenght += len(s)
        SN_lenght = AES.block_size - (tmp_lenght + len(email) + len(uid) + len(strangestr)) % AES.block_size
        SN = ''.join(random.choice(string.digits) for x in range(SN_lenght))

        #элементы обоих списков должны соотоветствовать друг другу
        value_list.append(email)
        value_list.append(uid)
        value_list.append(strangestr)
        value_list.append(SN)
        value_list.append('user')

        if len(items_list) == len(value_list):
            outs = ''
            for j in range(len(items_list)):
                outs += items_list[j] + value_list[j]
            return outs

print('Enter email')
while True:
    email = input()
    if len(email) != 0:
        break
    print('Enter email again')

#получение зашифрованного сообщения
profile = profile_for(email)
print(parse_to_json(profile))
plain_text = padding_str(profile, AES.block_size)
key = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(plain_text)


#получение блока замены шифртекста
foo_mail = 'admin@a.a'
l = len(foo_mail)
shift = 23 + l + (AES.block_size - (23 + l) % AES.block_size)
changing_str = profile_for(foo_mail)[shift: shift + AES.block_size]
mod_encrypted = encrypted[: len(encrypted) - AES.block_size] + cipher.encrypt(changing_str)
mod_decrypted = ''.join(chr(x) for x in checking_padding(cipher.decrypt(mod_encrypted)))
print(parse_to_json(mod_decrypted))


