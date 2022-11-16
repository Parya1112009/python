import pdb;
from array import *
def max_prod(arr1):
    maxi = 0
    
    for i in range(0, len(arr1)):
        for jo in range(1, len(arr1)):
             #pdb.set_trace()
             if (arr1[i]*arr1[jo]) >= maxi and (arr1[i] != arr1[jo]) :
                 #pdb.set_trace()
                 maxi = arr1[i]*arr1[jo]  
                 pairs = str(arr1[i]) +","+ str(arr1[jo])     
    return pairs
array1 = array('i',[1,2,90,3,4,5])
print (max_prod(array1))
