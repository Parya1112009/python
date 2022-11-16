import re
string = """The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48%-
the worst day since it launched in 1998 .\nThe panico****** 23456 selling prompted opnic by the co_ronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."""  
result = re.findall(r"\s", string)
#print (result)
result1 = re.findall(r"\S{8}", string)
result2 = re.findall(r"\w{8}", string)
result3 = re.findall(r"\D{8}", string)
print (result1,result2)
print("\n\n")
print(result3)