import pdb;
def dtob(num):
    if num==0:
       return 1
    else:
        return (num%2+10 * dtob(int(num/2))) 
print(dtob(40))
        