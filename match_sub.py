import re
text= "MY NAME is Priyanka"
pattern = r'[A-Z]{2,}'
print (pattern)
match = re.sub(pattern,"NAAM", text)
print (match)