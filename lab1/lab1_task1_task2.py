#RFC 2315 10.3

def padding_str(s, k):
    if k > 1 and k < 256:
        if type(s) != bytes:
            b_s = s.encode()
        else:
            b_s = s
        l = len(b_s)
        mod = k - l % k
        outs = b_s + (chr(mod) * mod).encode()
        return outs
'''
s = '12345678901'
s1 = padding_str(s, 11)
print(s1)
s1 = 'ICE ICE BABY\x05\x05\x05\x05\x05'
'''
def checking_padding(p_s):
    if p_s != None and len(p_s) > 1:
        if type(p_s) != bytes:
            b_p_s = p_s.encode()
        else:
            b_p_s = p_s
        lenght = len(b_p_s)
        p_sym = b_p_s[lenght - 1]
        if b_p_s[lenght - int(p_sym): ] == (chr(p_sym) * int(p_sym)).encode():
            return b_p_s[: lenght - int(p_sym)]

#s2 = checking_padding(s1)
#print(s2)
