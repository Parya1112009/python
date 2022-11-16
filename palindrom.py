def palindrom(string2):
    x = len(string2)
    for i in range(x-1):
        if string[i] == string[x-1]:
            x = x-1
        else:
            return "NOT PALINDROM" 
    return "PALINDROM"           
string = input("enter the string")
print (palindrom(string))  
