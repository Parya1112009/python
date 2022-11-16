import re
s = 'https://www.geeksforgeeks.org/'
s1 = 'pr//ya'
match1 = re.search(r'(\w+)//(\w+)',s1)
match = re.search(r'(\w+)://(\w{3}).(\w+).(\w{3})/', s)
match2 = re.findall(r'(\w+)://(\w{3}).(\w+).(\w{3})/', s)
print (match)
print(match1)
print(match2)
