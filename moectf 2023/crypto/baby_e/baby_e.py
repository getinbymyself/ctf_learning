import gmpy2
c =  147693154873835354725007152781732424355869776162377337823960431913672366269917723916891506269449726723757821517328874729037838600793748824028829185409932536014732765063216715033843955453706710187792772702199448156372644163429786386035008302836467605094954587157232829525150652611067567669525072625329634860065850520051628272535479197120008981979404760445193750864902244921407742155742716289495581989134730376783828846663464819337418977287363028738701414486788851136608957124505485242331701209645216580641917007780811842757125048746184068597664780265422321550909392419865169775282217442331295071069272774722564587602419768461231775480847018941840911357926330143045826277813722919121117172763493242590521245640828462665947672485094793188432098216701511715232654611338293295459889814699850788048985878279440740712956248569068077253790198036918598519191892836075254345518967666166925163908185663991353344555402397055977817370082929420443034626201745027965444069777059760865359310439815816749939498993014457995041394803598825093836045546578310632172636478575946653375857640993393714607308326474003446154152048840071034349831168612740218034679021240949747357214453636633636662650940968576792518622437627529244515229173
n =  553409369582823237678532685244026647155180191225879439432235077135813123637186465008813830373646133388592395760175777499266561095087891764348044063111935877931069321764391883899483374576303169645488542398590564148654412004383012178107972880058460460806768779452529433458826925606225797078653905380530651390617109384086518728626571028089036812787671647095695947167204428442727185744172445701874820612799168887428075695751162763647868386879374037826876671079326544820609721731078985096813307183878793033824330869698508952853770794414757655681370862323768018291030331209143189638496644361618184164228294031490537429556439588954274708598530042700988138862000054458742762198052079867259365645914383561162796796952346445529346145323567650621600171442575319262718389389870407629339714751583360252884338116164466349449862781112019462555743429653595045695696967783338371470032332852204294900011651434678829104876529439166176589508898757122660322523937330848536715937381297551894198974459004139082562228022412335520195652419375915216074658463954339332593244483927157329404652516225481116614815221154229491846087288087715884363786672244655901308480290011237244562251084095684531716327141154558809471185132979704992609461470501119328696999713829
e =  7
i=0
while 1:
    res = gmpy2.iroot(c+i*n,7)
    if(res[1] == True):
        m=res[0]
        print(hex(m))
        break
    print("i="+str(i))
    i = i+1