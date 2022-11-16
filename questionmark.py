import re
string = """The Euro STOXX 600 index, which Eb tracks all stock markets across Europe including the FTSE, fell by 11.48% –
the worst day since it launched in 1998 \n. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
match = re.findall(r'\d\d\d?', string, re.M)
print (match)
match = re.findall(r'E.? ', string, re.M)
print (match)
match = re.search(r'(E.?).*(E.+?).*(F.*?)', string, re.M)
match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')
print (match_object.group(1))
print (match.groups())
match = re.findall(r'E.*?', string, re.M)
print (match)
match = re.findall(r'E.+?', string, re.M)
print (match)