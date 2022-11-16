import pdb
list1 = []
list11 = []
count = 0
with open("dupli.txt","r") as f:
    for i in f.read().split():
        if i not in d:
            d[i] =count 
        if d.key(i):
           d[i] = count+1
print(d)
