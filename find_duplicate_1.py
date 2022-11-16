import pdb;
from array import *
def find_dup(arr1):
    listt = []
    for i in range(0, len(arr1)):
        count = 0
        for jo in range(1, len(arr1)):
             #pdb.set_trace()
             if (arr1[i]== arr1[jo]):
                 count +=1
        if count >1 and arr1[i] not in listt:
            #pdb.set_trace()
            listt.append(arr1[i])  
    return listt
array1 = array('i',[5,1,2,3,4,4,6,5,5,1,7,7,7,7,])
print (f"duplicate numbers are {find_dup(array1)}")
