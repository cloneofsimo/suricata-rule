import os
# check the requests with wget.

with open('./https.txt') as F:
    lis1 = F.read().splitlines()
    
with open('./http.txt') as F:

    lis2 = F.read().splitlines()
    
for lnk in lis1 + lis2:
    cmd = f'wget {lnk}'
    print(cmd)
    os.system(cmd)