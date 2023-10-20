from Crypto.Util.number import *
round = 2
#flag = open("./secret", "rb").read().strip()
def f(m, key):
    m = m ^ (m >> 4)
    m = m ^ (m << 5)
    m = m ^ (m >> 8)
    m ^= key
    m = (m * 1145 + 14) % 2**64
    m = (m * 1919 + 810) % 2**64
    m = (m * key) % 2**64
    return m
def enc(m, key, round):
    key = bytes_to_long(key)#key=8607905462700304239(19位)
    left = bytes_to_long(m[:8])
    right = bytes_to_long(m[8:])
    for i in range(round):
        left, right = right, f(right, key) ^ left
    left, right = right, left
    return long_to_bytes(left).rjust(8, b"\x00") + long_to_bytes(right).rjust(8, b"\x00")#rjust不足八位左边补\x00
def padding(m):#对于bytes类型的变量m，使得在其末尾填充pad个字节的pad
    mlen = len(m)
    pad = 16 - mlen % 16
    return m + pad * bytes([pad])
def ecb_enc(m, key):
    m = padding(m)
    mlen = len(m)
    c = b""
    for i in range(mlen // 16):
        c += enc(m[i * 16 : i * 16 + 16], key, round)
    return c
#print(ecb_enc(flag, b"wulidego"))#flag填充后有32位
c=b'\x0b\xa7\xc6J\xf6\x80T\xc6\xfbq\xaa\xd8\xcc\x95\xad[\x1e\'W5\xce\x92Y\xd3\xa0\x1fL\xe8\xe1"^\xad'
key=bytes_to_long(b"wulidego")
right0=bytes_to_long(c[:8])
left0=bytes_to_long(c[8:16])
right1=bytes_to_long(c[16:24])
left1=bytes_to_long(c[24:32])
flag1=right0 ^ f(left0,key)
flag0=left0 ^ f(flag1,key)
flag3=right1 ^ f(left1,key)
flag2=left1 ^ f(flag3,key)
flag=long_to_bytes(flag0)+long_to_bytes(flag1)+long_to_bytes(flag2)+long_to_bytes(flag3)
print(flag)
#运行结果：moectf{M@g1cA1_Encr1tion!!!}\x04\x04\x04\x04
#flag:moectf{M@g1cA1_Encr1tion!!!}