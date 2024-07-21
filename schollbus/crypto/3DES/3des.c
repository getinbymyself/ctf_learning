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
int main(void){
    int i;
    uc bufout[8] = {0xf6,0xff,0x60,0xa7,0xd1,0xc3,0x94,0x90};//f6ff60a7d1c39490
    uc bufin[8] = {0};
    uc cal[8],tmp[8];
    uc key1[] = "AAA{xxxx";
    uc key2[] = "x_xyxxy}";
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
    for(int j = 0;j < size;j++){
        for(i=0;i<8;i++){
            printf("%02x",valuespace1[j][i]);
        }
        printf("\n");
    }
    return 0;
}