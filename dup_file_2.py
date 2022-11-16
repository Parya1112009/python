import pdb
import re
listt = []
count = 0
l = []
#pdb.set_trace()
with open("dupli.txt","r") as f:
    for i in f.read().split():
        #pdb.set_trace()
        listt.append(i)
print(listt)
