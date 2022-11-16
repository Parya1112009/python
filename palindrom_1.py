import pdb
def palindrom(string2):
    x = len(string2)/2
    for i in range(int(x)):
        #pdb.set_trace()
        if string2[i] != string2[-i-1]:
            return "NOT PALINDROM" 
    return "PALINDROM"           
string = input("enter the string\n")
print (palindrom(string))  

