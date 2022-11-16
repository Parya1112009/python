import pdb
kys = []
vlues = []
d1 = {} 
with open("eva.txt","r") as f:
  for i in f.readline().split():
    kys.append(i)
  for i in f:
    pdb.set_trace() 
    vlues.append(i.split())
print (kys)
#print (vlues)
