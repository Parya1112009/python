import re
text = "India"
match = re.search(r'india', text, re.I)
match = re.search(r'india', text)
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
string2 = re.search(r""".+\s #Beginning of the string
			(.+ex) #Searching for index
			.+ #Middle of the string
			(\d\d\s.+). #Date at the end""",string,re.X)
print (string2.group(1),string2.group(2))        
match = re.search(r'.*', string, re.S)
match1 = re.search(r'.*', string, re.S)
#match = re.search(r'.*', string, re.S) ##need to find why .* is not returning the whole string..it wrks when i put brackets(use group method)
print (match.group(0))
#print (match1)
