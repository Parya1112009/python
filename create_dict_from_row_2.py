import re
import pdb
do = {}
listall = []

keys = []
values = []
with open("sample2.txt","r") as f:
    for li in f:
        key = re.findall(r'\w{2,}', li)
        keys.append(key[0])
        values.append(key[1::])
for i in range(len(values)):
    for jo in range(len(values[i])):
        pdb.set_trace()
        do[keys[i]] = values[i][jo]
        listall.append(do)
print (do)        
