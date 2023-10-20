import os
import subprocess
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}"
flag="moectf{"
for i in range(100):
    if flag[-1]=="}":
        break
    for j in range(64):
        temp=flag+alpha[j]
        result=subprocess.run(['smc.exe'], input=temp, text=True, capture_output=True)
        if result.stdout=='Plz input your flag:\nGOOD':
            flag=temp
            print(flag)
            break


