import re
p = tuple(re.findall(r'\d{4}$|\d{3}', '0123456789'))
print (p)