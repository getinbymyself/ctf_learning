# coding='utf-8'
"""
判断文件是否是伪加密
有两个加密表示位：
第一个：文件[6:8]
第二个：文件目录区,504B0102开头，再也8，9位
第一个：第二个：是否加密
0000:0000:没有加密
0000:0900:伪加密
0900:0900:真加密
0900:0000:没有加密
使用方法：python3 is_pe filename.zip
"""
import sys
import os

def is_pe(file):
    flag_pe_top = b'PK\x01\x02'
    flag_te = b'\t\x00'
    flag_ne = b'\x00\x00'

    with open(file, 'rb') as f:
        text = f.read()
        
    flag_index = text.find(flag_pe_top)
    if  text[6:8] == flag_ne and text[flag_index+8:flag_index+10] == flag_te:
        return 1
    elif text[6:8] == flag_te and text[flag_index+8:flag_index+10] == flag_te:
        return 0
    elif text[6:8] == flag_ne and text[flag_index+8:flag_index+10] == flag_ne:
        return -1
    elif text[6:8] == flag_te and text[flag_index+8:flag_index+10] == flag_ne:
        return -1
    else:
        return -2


def main():
    if len(sys.argv) != 1:
        for arg in sys.argv[1:]:
            flag = is_pe(arg)
            if flag == 1:
                print("[+] %s 是伪加密！"%arg)
            elif flag == 0:
                print("[*] %s 是真加密"%arg)
            elif flag == -1:
                print("[#] %s 文件无加密"%arg)
            else:
                print("[-] %s 文件损坏"%arg)
    else:
        print('help: python3 is_pe file1 file2 file3')


if __name__ == '__main__':
    main()