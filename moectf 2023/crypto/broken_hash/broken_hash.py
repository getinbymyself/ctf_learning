def F(x, y, z):
    return ((x & ~y) ^ (y & ~z) ^ (z & ~x)) ^ (
        ((x + y) * (y + z) + (x + z)) & 0xFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF
    )
def _block_hash(a, b, c, d):#c,d,a,b
    x, y, z, w = F(a, b, c), F(b, c, d), F(c, d, a), F(d, a, b)
    return (a ^ b ^ c ^ d ^ x ^ y ^ z ^ w) ^ 0xFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF
def _hash(blocks: list[int]):
    length = len(blocks)
    print(length)
    if length % 4 != 0:
        padding = 4 - length % 4
        blocks += [0] * padding
        length += padding
    if length == 4:
        return _block_hash(*blocks)
    else:
        block_size = length // 4
        h1 = _hash(blocks[:block_size])
        h2 = _hash(blocks[block_size : block_size * 2])
        h3 = _hash(blocks[block_size * 2 : block_size * 3])
        h4 = _hash(blocks[block_size * 3 :])
        return _block_hash(h1, h2, h3, h4)
def bytes2blocks(data: bytes, block_size=16):
    if len(data) % block_size != 0:
        data += b"\x00" * (block_size - len(data) % block_size)
    return [
        int.from_bytes(data[i : i + block_size], "little")
        for i in range(0, len(data), block_size)
    ]
def hash(*data: list[bytes]):
    return _hash(bytes2blocks(b"".join(data)))
from typing import Callable
from random import randbytes
from base64 import b64decode,b64encode
from hashlib import md5
from string import ascii_letters
from random import choices
# with open("flag.txt", "r") as f:
#     flag = f.read().strip()
# def chall(input: Callable[[str], None], print: Callable[[str], None]):
#     def proof_of_work():

#         s = "".join(choices(ascii_letters, k=16))
#         h = md5(s.encode()).hexdigest()
#         print(f"<!> md5(XXXXXXXX+{s[8:]}) == {h}")
#         i = input("Give me XXXXXXXX: ")
#         return md5((i + s[8:]).encode()).hexdigest() == h
#     if not proof_of_work():
#         print("<!> ACCESS DENIED <!>")
#         return

#     b = randbytes(256)
#     print(f"this is a random bytes: {b64encode(b).decode()}")
#     i = input("give me another bytes with the same hash: ")
#     try:
#         d = b64decode(i)
#     except:
#         print("invaild input")
#     if hash(b) == hash(d) and d!=b:
#         print(f"congurations! and your flag is {flag}")
from pwn import *
from pwnlib.util.iters import mbruteforce
import string
from hashlib import md5
import functools
import math
import gmpy2
#context.log_level="debug"
p=remote("172.26.208.1",57247)
p.recvuntil(b"XXX+")
y=p.recvuntil(b")")
y=y[:-1]
p.recvuntil(b" == ")
s=p.recvuntil(b"\n")
s=s[:-1]
print(y)
print(s)
send=mbruteforce(lambda x:md5(x.encode()+y).hexdigest()==s.decode(),string.ascii_letters+string.digits,length=4)
p.sendline(send.encode())
p.recvuntil(b"bytes: ")
recv=p.recvuntil(b"\n")
recv=recv[:-1]
b=b64decode(recv)
f=b""
for i in range(4):
    f+=b[(4*i+2)*16:(4*i+2)*16+16]
    f+=b[(4*i+3)*16:(4*i+3)*16+16]
    f+=b[(4*i+0)*16:(4*i+0)*16+16]
    f+=b[(4*i+1)*16:(4*i+1)*16+16]
send=b64encode(f)
p.sendline(send)
p.interactive()