import pdb;
def int_rev(d):
    n = str(d)
    x = len(n) 
    rev = ''
    for i in range(x-1, -1, -1):
        rev += n[i]   
    return rev    
num = input("enter the number")
print (int_rev(num))
