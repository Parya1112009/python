import re
string = """The Euro STOXX                 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48%-
the worst day since it launched in 1998 .\nThe panico 23456 selling index prompted opnic by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
result = re.findall(r"\s(\w{1,2})\s", string)
print(string.count("index"))
print (result)
print ("\n\n")
result = re.findall(r"\W", string)
print (result)
