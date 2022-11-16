import re
with open("dupli.txt","r") as f:
    listt = f.readline().split(" ")
l = []
c = 0
li = []
for i in listt:
    count = 0
    if i not in li:
       li.append(i)
    elif i in li and li.count(i)>=1:
       print(f"{i} came {li.count(i)} times")


