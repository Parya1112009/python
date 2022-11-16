import pdb
import re
listt = []
count = 0
l = [] 
#pdb.set_trace()
with open("dupli.txt","r") as f:
  for i in f.read().split():
    pdb.set_trace()
    listt.append(i)
for j in listt:
  count = 0  
  for k in range(len(list)):
    if j == listt[k] and j not in l: 
      count = count+1
    if k==len(listt)-1 and count>1:  
      #print "{0} has come {1} times in the file".format(j, count)
      l.append(j)
print (l)