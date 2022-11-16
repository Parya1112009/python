import re
text= "MY NAME is Priyanka"
string = "priyanka arya"
pattern = r'[a-z]{2,6}'
print (pattern)
#match = re.sub(pattern,"NAAM", text)
match = re.sub('MY',"NAAM", text)
print(string.replace("arya","panwar",1))
print(string.split("k"))
print (match)