#RFC 2315 10.3

def padding_str(s, k):
    if k > 1 and k < 256:
        l = len(s)
        mod = k - l % k
        outs = s + str(chr(mod)) * mod
        return outs

s = 'YELLOW SUBMARINE'
s1 = padding_str(s, 20)
print(s1)
s1 = 'ICE ICE BABY\x05\x05\x05\x05\x05'

def checking_padding(p_s):
    if p_s != None and len(p_s) > 1:
        lenght = len(p_s)
        p_sym = p_s[lenght - 1]
        num_p_sym = ord(p_sym)
        if str(p_s[lenght - num_p_sym: ]) == str(p_sym) * num_p_sym:
            return p_s[: lenght - num_p_sym]

s2 = checking_padding(s1)
print(s2)
