import pdb
import re
phone = "(914).234.2312"
string = re.split('\.',phone)
str = []
for i in range(len(string)):
    str.append(string[i].strip('(').strip(')'))
print ('.'.join(str))


