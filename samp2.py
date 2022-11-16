
import os
import pdb
path = os.getcwd()
pdb.set_trace()
path2 = os.chdir("sample2")
if os.path.exists("priya.txt"):
  print ("it exists")
else:
  print ("it does not exist")
#print os.path.dirname(path)
#print os.path.basename(path)
#print os.path.isfile(path)
#print os.path.isdir(path)
#print os.path.ismount(path)
#print os.listdir(path)
