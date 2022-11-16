import re
string = """The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% –
the worst day since it launched in 1998 .\nThe pnicp 23456 selling prompted opnic by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
result = re.findall(r"\b\d{4}\b", string, re.M)
print(result)
result = re.findall(r"\Bnic\B", string, re.M)
print(result)

#/b is used for word boundry where as /B is used for finding the pattern which is not a word for ex: above string 
#has panico since i used /B front n end so it will find a match 