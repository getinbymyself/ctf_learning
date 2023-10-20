from Crypto.Util.number import isPrime
from random import getrandbits
with open("flag.txt","rb") as fs:
    flag = fs.read().strip()
def diffie_hellman(p, flag):
    alice_privKey = getrandbits(1024)
    alice_pubKey = pow(7, alice_privKey, p)
    bob_privKey = getrandbits(1024)
    bob_pubKey = pow(7, bob_privKey, p)

    superkey = pow(bob_pubKey, alice_privKey, p)
    m = int.from_bytes(flag, 'big')
    return (m * superkey) % p, alice_pubKey, bob_pubKey
from typing import Callable
def chall(input:Callable[[str],None], print:Callable[[str],None]):
    p = int(input("P = "))
    if isPrime(p) and p.bit_length() >= 1024:
        c, alice_pubKey, bob_pubKey = diffie_hellman(p, flag)
        print("Alice's public key: {}".format(alice_pubKey))
        print("Bob's public key: {}".format(bob_pubKey))
        print("Ciphertext: {}".format(c))
    else:
        print("Invalid P")
# from random import choice
# from Crypto.Util.number import isPrime, sieve_base as primes
# def myPrime(bits):
#     while True:
#         n = 2
#         while n.bit_length() < bits:
#             n *= choice(primes)
#         if isPrime(n + 1):
#             return n + 1
# print(myPrime(1024))
#pohlig_hellman(构造光滑p)
p=2671189896155050966860419911550296655622712287511639338826974133799750925030911241649295217539575267264547565233650183739647054794634637840582038856045767858855463438059436392971488398287253297339900323428229106602693860131156649376313270986483215659658747861356389943648741911333951037060511811120779591931407
apub=2078581708387983693173164765947753819775284268912939270544697744549946841712647724558191223970687897609818559214064718288865685266966229026026462866396528873230949566462547098522923210956606684755254113945638789898135809088499014799206824657266401344908809235583213460459705826164920102000738389561817265815432
bpub=1204676179266468254173444572461785353282607720263558224557765810376135324152001810873855526385919246167454627473244983983978427702423894959281680858658035576390215971027901451218537483960894084448980732684711642530402265729231067776479960348403949765451509925089632253502795878842947760429266764808387325278533
c=550800217467472165228930180586797418389277325611879748238647665730534413045175383653702905602590583141536394184019239464870588262845306338982154998933260739195961682943788192880140908654064486684228901167491843998274199454303916076681249004373822158756406637370186423629629267088854743256352754444804405044503
apri=175347156273409278779450023537285492728144840381860525356455113677882188874941514355013828807097773451454270556638122339291394921328451077723022666946035550287456076049766466200034332530265399814757338492051465247659808320280270475088326134413216680679662068553697419613616939133815840956995213534159522604461
bpri=178544100401894803143840055060754113941902374247562824632900405774815667260922583712932389787846707817028002196602382766871926661881377685424356912549499060761031151516956887474065714579227189927240318811312877163761145380909966641500276443076257132333196607218461202303086655983960035502242124652998880908581
super=1166488662729631443777458421726103833375138994842167944465992829430876826763986168588434307457163311345380351947128916183539571197053191277881823052979836953193051427035066217521100707518722074257918930701228906403908053021575479234384471471773019164332796690526286538694462872901457379385572996846001243067822
#flag:moectf{diffie_he11man_key_exChange_is_not_so_hard_2WPIBung92WPIBung9?WP}