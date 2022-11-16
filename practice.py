import re
text= """The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by"
the worst day since it launched in 1998 hig\n. panic 23456 selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 february"""  
#text = "MY name IS OPU"
#match = re.search(r'([^A-Z]{4,})', text) #not in the range A-Z
#match1 = re.search(r'(^[A-Z]{2,})', text)
#match2 = re.search(r'([A-Z]{2,}$)', text)
match3 = re.search(r'([a-z]{2,5})$', text, re.M)
match3 = re.search(r'([a-z]{2,5})$', text, re.M)
#match3 = re.search(r'([a-z]{3,5})\Z', text)
#print (match.groups())
#print (match1.groups())
print (match3.groups())

