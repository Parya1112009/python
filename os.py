import re
import os 
path = os.getcwd()  
print(path)
for i in os.listdir(path): 
  if i.endswith(".py"): 
    print(i)
  elif i.startswith("math"):
    print(i) 
     

