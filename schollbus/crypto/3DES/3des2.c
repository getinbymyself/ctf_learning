#include <stdio.h>
#include <string.h>
#include <openssl/des.h>
#include <stdlib.h>
typedef unsigned char uc;
void encrypt(unsigned char bufin[], unsigned char bufout[], unsigned char key[])
{
    DES_cblock *pin, *pout;
    DES_key_schedule ks;
    pin = (DES_cblock*)bufin;
    pout = (DES_cblock*)bufout;
    des_set_key((DES_cblock *)key, ks);
    des_ecb_encrypt(pin, pout, ks, DES_ENCRYPT);
}
void decrypt(unsigned char bufin[], unsigned char bufout[], unsigned char key[])
{
    DES_cblock *pin, *pout;
    DES_key_schedule ks;
    pin = (DES_cblock*)bufin;
    pout = (DES_cblock*)bufout;
    des_set_key((DES_cblock *)key, ks);
    des_ecb_encrypt(pin, pout, ks, DES_DECRYPT);
}
int compare(const void *arg1, const void *arg2) {
    uc *a = (uc*)arg1;
    uc *b = (uc*)arg2;
    int i;
    int result = 0;
    for(i=0;i<8;i++){
        if(a[i] > b[i]){
            result = 1;
            break;
        }
        else if(a[i] < b[i]){
            result = -1;
            break;
        }
        else{
            continue;
        }
    }
    //int result = strcmp(a, b);
    if (result > 0) {
        return 1;
    }
    else if (result < 0) {
        return -1;
    }
    else {
        return 0;
    }
}
// int searchstr(int * list,int len,int target){
//     int low = 0;
//     int hight = len-1;
//     int middle;
//     while(low <= hight){
//         middle = (low + hight)/2;
//         if(list[middle] = target)
//         {
//             printf("已找到该值，数组下标为:%d\n",middle);
//             return list[middle];
//         }
//         else if(list[middle] > target)
//         {
//             hight = middle -1;
//         }
//         else if(list[middle] < target)
//         {
//             low = middle + 1;
//         }
//     }
//     printf("未找到该值");
//     return -1;
// }
int searchstr(uc value[][8], int size,uc *n) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (compare(value[mid],n) > 0) {
            right = mid - 1;
        }
        else if (compare(value[mid],n) < 0) {
            left = mid + 1;
        }
        else{
            return mid;
        }
    }
    return -1;
}
int main(void){
    int i;
    uc bufout[8] = {0xf6,0xff,0x60,0xa7,0xd1,0xc3,0x94,0x90};//f6ff60a7d1c39490
    uc bufin[8] = {0};
    uc cal[8],tmp[8];
    uc key1[] = "AAA{wwww";
    uc key2[] = "x_xyxxy}";
    uc cmp[] = {0x7f,0xfe,0xa9,0xa8,0x51,0x47,0xa3,0x47};
    static uc valuespace1[26*26*26*26*26][8] = {0};
    int size = sizeof(valuespace1) / sizeof(valuespace1[0]);
    int t = 0;
    for(key2[0] = 'a';key2[0] <= 'z';key2[0]++){
        for(key2[2] = 'a';key2[2] <= 'z';key2[2]++){
            for(key2[3] = 'a';key2[3] <= 'z';key2[3]++){
                for(key2[4] = 'a';key2[4] <= 'z';key2[4]++){
                    for(key2[5] = 'a';key2[5] <= 'z';key2[5]++){
                        key2[6] = key2[3];
                        decrypt(bufout,cal,key2);
                        for(i=0;i<8;i++){
                            valuespace1[t][i] = cal[i];
                        }
                        t++; 
                    }
                }
            }
        }
    }
    qsort(valuespace1, size , 8, compare);
    //uc vspace[62] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    uc key[16];
    int index[4];
    int nn;
    for(index[0] = 0;index[0] < 62;index[0]++){
        for(index[1] = 0;index[1] < 62;index[1]++){
            for(index[2] = 0;index[2] < 62;index[2]++){
                for(index[3] = 0;index[3] < 62;index[3]++){
                    uc vspace[62] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    char kind[3] = {0,0,0};
                    for(i = 0;i < 4;i++){
                        key1[i+4] = vspace[index[i]];
                        if(key1[i+4] >= '0' && key1[i+4] <= '9')
                            kind[0]++;
                        else if(key1[i+4] >= 'A' && key1[i+4] <= 'Z')
                            kind[1]++;
                        else
                            kind[2]++;
                    }
                    if(kind[0] == 0 || kind[1] == 0 || kind[2] == 0)
                        continue;
                    encrypt(bufin,tmp,key1);
                    nn = searchstr(valuespace1,size,tmp);
                    if(nn > 0){
                        memset(key,0,16);
                        strcpy(key,key1);
                        for(key2[0] = 'a';key2[0] <= 'z';key2[0]++){
                            for(key2[2] = 'a';key2[2] <= 'z';key2[2]++){
                                for(key2[3] = 'a';key2[3] <= 'z';key2[3]++){
                                    for(key2[4] = 'a';key2[4] <= 'z';key2[4]++){
                                        for(key2[5] = 'a';key2[5] <= 'z';key2[5]++){
                                            key2[6] = key2[3];
                                            decrypt(bufout,cal,key2);
                                            if(compare(valuespace1[nn],cal) == 0){
                                                strcat(key,key2);
                                                puts(key);
                                                goto begin;
                                            }
                                        }
                                    }
                                }
                            }
                        }   
begin:     
                    }
                }
            }
        }
    }
    
out:
    return 0;
}