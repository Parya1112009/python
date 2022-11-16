import pdb;
import re
def dtob(num,listt = []):
    if num == 0:
        return 1
    else:
        listt.append(num%2)    
        dtob(int(num/2))
    return listt    
x = dtob(40)
print(x)
x2 = ''.join(str(i) for i in x)
print (x2)





        
        