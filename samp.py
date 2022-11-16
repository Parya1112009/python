import os
pwd = os.getcwd()
for i in os.listdir(pwd):
    if i.endswith(".txt"):
       print (i) 
