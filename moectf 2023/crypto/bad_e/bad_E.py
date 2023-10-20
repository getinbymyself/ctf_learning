#AMM算法（可见https://github.com/C0nstellati0n/NoobCTF/blob/42e00a465ae7045f0fd045304daa671428f6b3e0/CTF/moectf/Crypto/signin.md）
from Crypto.Util.number import *
from sympy.ntheory.residue_ntheory import nthroot_mod
e = 65537
p=6853495238262155391975011057929314523706159020478084061020122347902601182448091015650787022962180599741651597328364289413042032923330906135304995252477571
q=11727544912613560398705401423145382428897876620077115390278679983274961030035884083100580422155496261311510530671232666801444557695190734596546855494472819
c=63388263723813143290256836284084914544524440253054612802424934400854921660916379284754467427040180660945667733359330988361620691457570947823206385692232584893511398038141442606303536260023122774682805630913037113541880875125504376791939861734613177272270414287306054553288162010873808058776206524782351475805
n=p*q
print(long_to_bytes(nthroot_mod(c,e,p)))