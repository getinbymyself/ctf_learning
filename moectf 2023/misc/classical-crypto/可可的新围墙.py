s="mt3_hsTal3yGnM_p3jocfFn3cp3_hFs3c_3TrB__i3_uBro_lcsOp}e{ciri_hT_avn3Fa_j"
flag=[0]*72
for i in range(72):
    if i%2==1:
        flag[i]=s[int((i+35)/2)]
    elif i%4==0:
        flag[i]=s[int(i/4)]
    elif i%4==2:
        flag[i]=s[int((i+214)/4)]
flag_of_fence=""
for i in range(72):
    flag_of_fence+=flag[i]
print(flag_of_fence)