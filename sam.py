import re
with open("dupli.txt","r") as f:
    list = f.read( )
listt = re.split("\s",list)
print(listt)
