import re
#match1 = re.compile(r'(^[a-z0-9_%+-]+@[a-z0-9.-]+\.[a-z]+$)')
match1 = re.compile(r'(^[a-z0-9_%+-]+@[a-z0-9]+\.[a-z]+$)')
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#print match1.search("priyankaarya@gmail..com").group() 
print match1.search("priyankaarya@gmail.com").group() 

