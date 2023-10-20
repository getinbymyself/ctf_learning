#进制转换后开头相同，随便代一个72位的值进去就可以得到key了（啊啊啊，为什么做了这么久！！！）
from Crypto.Util.number import *
# with open("key.txt", "r") as fs:
#     key = int(fs.read().strip())
# with open("flag.txt", "rb") as fs:
#     flag = fs.read().strip()
# assert len(flag) == 72
# m = bytes_to_long(flag)
base = bytes_to_long(b"koito")
iv = 3735927943
def blockize(long):
    out = []
    while long > 0:
        out.append(long % base)
        long //= base
    return list(reversed(out))
# blocks = blockize(m)
def encrypt_block_cbc(blocks, iv, key):
    encrypted = [iv]
    for i in range(len(blocks)):
        encrypted.append(blocks[i] ^ encrypted[i] ^ key)
    return encrypted[1:]
key=421036458
c=[8490961288, 122685644196, 349851982069, 319462619019, 74697733110, 43107579733, 465430019828, 178715374673, 425695308534, 164022852989, 435966065649, 222907886694, 420391941825, 173833246025, 329708930734]
length=15
init=pow(base,length-1)
power=[0]*15
for i in range(1,length):
    power[i]=pow(base,length-i-1)
power[0]=init
while True:
    b=[0]*15
    b[0] = c[0] ^ key ^ iv
    sum=b[0] * power[0]
    for i in range(1,length):
        b[i] = c[i] ^ c[i-1] ^ key
        sum=sum+b[i]*power[i]
    flag=long_to_bytes(sum)
    key+=1
    if flag.startswith(b"moe"):
        print(flag)
        break
print(flag)
    