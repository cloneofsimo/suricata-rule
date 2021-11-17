
sid_counter = 1000

with open('./https.txt') as F:
    lis = F.read().splitlines()
    for lnk in lis:
        sid_counter +=1
        rule = f'alert tcp any any -> any 443 (msg:"HTTPS {lnk} access"; tls.sni; content:"{lnk}"; nocase; sid:{sid_counter}; rev:1;)'
        print(rule)

with open('./http.txt') as F:
    lis = F.read().splitlines()
    for lnk in lis:
        sid_counter +=1
        rule = f'alert tcp any any -> any 80 (msg:"HTTP {lnk} access"; content: "GET /"; content:"{lnk}"; sid:{sid_counter}; rev:1;)'
        print(rule)