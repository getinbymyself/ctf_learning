# import random
# with open("flag.txt", "r") as f:
#     flag = f.read().strip()
# class LCG:
#     def set_params(self):
#         self.m = random.randint(10000, 20000)
#         self.a = random.randint(10000, 20000)
#         self.c = random.randint(1, self.a-1)
#         self.x = random.randint(0, self.m-1)
#     def get_all_output(self):
#         x0 = self.x
#         s = set()
#         while (t := self()) not in s:
#             s.add(t)
#         self.x = x0
#         return s
#     def __init__(self):
#         self.set_params()
#         while len(self.get_all_output()) < 10:
#             self.set_params()
#     def __call__(self):
#         self.x = (self.a * self.x + self.c) % self.m
#         return self.x
# from typing import Callable
# def chall(input:Callable[[str],None], print:Callable[[str],None]):
#     from hashlib import md5
#     from string import ascii_letters
#     s = "".join(random.choices(ascii_letters, k=16))
#     h = md5(s.encode()).hexdigest()
#     print(f"<!> md5(XXXXXXXX+{s[8:]}) == {h}")
#     i = input("Give me XXXXXXXX: ")
#     if md5((i + s[8:]).encode()).hexdigest() != h:
#         print("<!> ACCESS DENIED <!>")
#         return
#     inst = LCG()
#     print("Let's play a simple game! If you can guess the right number, I will give your the flag! You have 10 tries")
#     for tries in range(10):
#         i = input(f"Give me a number, you have failed for {tries} times: ")
#         if int(i) == (right := inst()):
#             print(f"Congurations! You win the game! Your flag is here: {flag}")
#         else:
#             print(f"Oh, you are wrong! The right number is {right}")
#攻击线性同余生成器
from pwn import *
from pwnlib.util.iters import mbruteforce
import string
from hashlib import md5
import functools
import math
import gmpy2
def _crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment
def _crack_unknown_multiplier(states, modulus):
    a = (states[2] - states[1])
    inv = int(gmpy2.invert(states[1]-states[0] % modulus, modulus))
    multiplier = (a * inv) % modulus
    return _crack_unknown_increment(states, modulus, multiplier)
def _crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:],diffs[2:])]
    modulus = abs(functools.reduce(lambda x,y: math.gcd(x,y),zeroes))
    return _crack_unknown_multiplier(states, modulus)
def crack(seq):
    return _crack_unknown_modulus(seq)
#context.log_level="debug"
p=remote("172.26.208.1",54682)
p.recvuntil(b"XXX+")
y=p.recvuntil(b")")
y=y[:-1]
p.recvuntil(b" == ")
s=p.recvuntil(b"\n")
s=s[:-1]
print(y)
print(s)
send=mbruteforce(lambda x:md5(x.encode()+y).hexdigest()==s.decode(),string.ascii_letters+string.digits,length=4)
p.sendline(send)
list=[]
for i in range(6):
    p.recvuntil(b"times: ")
    p.send(b"1\n")
    p.recvuntil(b"number is ")
    s=p.recvuntil(b"\n")
    s=s[:-1]
    temp=int(s.decode())
    list.append(temp)
result=_crack_unknown_modulus(list)
n=result[0]
a=result[1]
b=result[2] 
flag=(a * list[5]+b) % n
flag=str(flag).encode()
p.sendline(flag)
p.interactive()