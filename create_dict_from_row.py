import re
import pdb
d = {}
listall = []
with open("sample2.txt","r") as f:
    for li in f:
        key = re.findall(r'\w{2,}', li)
        d[key[0]] = key[1::]
print (d)        
