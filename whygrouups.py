import re
string = string = "The Euro STOXX 600 index-$-2# which %-\n tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
match = re.findall(r"\w*", "name is priyanka name")
result = re.search(r"\W\D\W", string)
result1 = re.findall(r"\W\D\W", string)
#print (match)
#print (result)
print (result.group())
print (result1)


