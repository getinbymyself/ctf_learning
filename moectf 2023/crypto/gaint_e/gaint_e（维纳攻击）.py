'''from Crypto.Util.number import getPrime

with open("flag.txt","rb") as fs:
    flag = fs.read().strip()

p = getPrime(1024)
q = getPrime(1024)
n = p * q
m = int.from_bytes(flag,"big")
c = pow(m,e,n)'''
import gmpy2
from Crypto.PublicKey import RSA
import ContinuedFractions, Arithmetic
from Crypto.Util.number import long_to_bytes 
 
def wiener_hack(e, n):
    # firstly git clone https://github.com/pablocelayes/rsa-wiener-attack.git !
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            discr = s * s - 4 * n
            if (discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d
    return False
e=0x609778981bfbb26bb93398cb6d96984616a6ab08ade090c1c0d4fedb00f44f0552a1555efec5cc66e7960b61e94e80e7483b9f906a6c8155a91cdc3e4917fa5347c58a2bc85bb160fcf7fe98e3645cfea8458ea209e565e4eb72ee7cbb232331a862d8a84d91a0ff6d74aa3c779b2b129c3d8148b090c4193234764f2e5d9b2170a9b4859501d07c0601cdd18616a0ab2cf713a7c785fd06f27d68dff24446d884644e08f31bd37ecf48750e4324f959a8d37c5bef25e1580851646d57b3d4f525bc04c7ddafdf146539a84703df2161a0da7a368675f473065d2cb661907d990ba4a8451b15e054bfc4dd73e134f3bf7d8fa4716125d8e21f946d16b7b0fc43
n=0xbaa70ba4c29eb1e6bb3458827540fce84d40e1c966db73c0a39e4f9f40e975c42e02971dab385be27bd2b0687e2476894845cc46e55d9747a5be5ca9d925931ca82b0489e39724ea814800eb3c0ea40d89ebe7fe377f8d3f431a68d209e7a149851c06a4e67db7c99fcfd9ec19496f29d59bb186feb44a36fe344f11d047b9435a1c47fa2f8ed72f59403ebb0e439738fd550a7684247ab7da64311690f461e6dce03bf2fcd55345948a3b537087f07cd680d7461d326690bf21e39dff30268cb33f86eeceff412cd63a38f7110805d337dcad25e6f7e3728b53ca722b695b0d9db37361b5b63213af50dd69ee8b3cf2085f845d7932c08b27bf638e98497239
c=0x45a9ce4297c8afee693d3cce2525d3399c5251061ddd2462513a57f0fd69bdc74b71b519d3a2c23209d74fcfbcb6b196b5943838c2441cb34496c96e0f9fc9f0f80a2f6d5b49f220cb3e78e36a4a66595aa2dbe3ff6e814d84f07cb5442e2d5d08d08aa9ccde0294b39bfde79a6c6dcd2329e9820744c4deb34a039da7933ddf00b0a0469afb89cba87490a39783a9b2f8f0274f646ca242e78a326dda886c213bc8d03ac1a9150de4ba08c5936c3fe924c8646652ef85aa7ac0103485f472413427a0e9d9a4d416b99e24861ca8499500c693d7a07360158ffffa543480758cafff2a09a9f6628f92767764fa026d48a9dd899838505ae16e38910697f9de14
d = wiener_hack(e, n)
m = pow(c,d,n)
print(m)