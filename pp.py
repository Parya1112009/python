import pdb;
def int_rev(t):
    #pdb.set_trace()
    rem = 0
    rev = 0
    tt = int(t)
    while tt>0:
        rem = tt%10
        rev= rem+rev*10
        tt = tt/10
        tt = int(tt)
    return rev  
num = input("enter the number")
#pdb.set_trace()
print (int_rev(num))

