import re
pattern = r'\d+'
print (pattern)
string = "67 years 36 old"
#match = re.match(pattern,string)
#match = re.search(pattern,string)
match = re.findall(pattern,string)
#match = re.finditer(pattern,string)
if match:
    print (match)
    #print(f"{match.group(0)} at index {match.start()}")
else:
    print("oops")