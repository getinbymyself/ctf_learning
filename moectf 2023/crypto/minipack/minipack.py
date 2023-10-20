from gmpy2 import *
from Crypto.Util.number import *
from Crypto.Util.number import long_to_bytes
key = eval(open("key.txt",'r').read())
c = int(open("ciphertext.txt","r").read())
m = ''
for i in reversed(key):
    if c>i:
        m += '1'
        c -= i
    else:
        m += '0'
end=len(m)
x=m[end-9:7:-1]
flag=long_to_bytes(int(x,2))
print(flag.decode())
