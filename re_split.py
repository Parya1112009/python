import re
pattern = r','
text = "i,am,priya,eva,neha"
match = re.split(pattern,text)
print (match)