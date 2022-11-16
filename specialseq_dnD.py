import re
string = """The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48%-
the worst day since it launched in 1998 .\nThe panico 23456 selling prompted opnic by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
result = re.findall(r"\d[a-z]{2}", string, re.M)
print(result)
result = re.findall(r"\W\D\W", string)
# in above pattern we are matching only \W\D\W
print(result)
result = re.findall(r"\W(\D)\W", string)
# in above pattern we are matching only \D
print(result)
#/b is used for word boundry where as /B is used for finding the pattern which is not a word for ex: above string 
#has panico since i used /B front n end so it will find a match 
#W = not 0-9,a-z,A-Z