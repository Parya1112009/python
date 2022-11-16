import re
import pdb
match1 = re.match(r'^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$',"excellent.priya@gmail.com")
pdb.set_trace()
print (match1)
