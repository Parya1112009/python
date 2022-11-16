import pdb
import re
phone = "914.234.2312"
#string = re.sub('\w{3}',"xxx",phone,2)
#string = re.sub('\d{3}',"xxx",phone,2)
string = re.sub('[0-9]{3}',"xxx",phone,2)
print (string)


