import re
import pdb
s = '作法 is Pythonic in Japanese'
#pattern = r'(\b\w{2}\b)'
pattern = r'\b\w{2}\b'
#pdb.set_trace()
li = re.search(pattern, s)
print(li.group(1))