import re
string = """The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% –
the worst day since it launched in 1998 .\nThe panic 23456 selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
result = re.findall(r"^([A-Z].*?)\s", string, re.M)
print (result)
result = re.findall(r"\A([A-Z].*?)\s", string, re.M)
print (result)
##\A will search only at the begining of the string but ^ will search at the begining of each line.
result = re.findall(r"\W\Z", string, re.M)
print(result)
result = re.findall(r"\W$", string, re.M)
print(result)
result = re.findall(r"[A-Z]|[a-z]", string, re.M)
result = re.findall(r"\b\d{4}\b", string, re.M)
print(result)
