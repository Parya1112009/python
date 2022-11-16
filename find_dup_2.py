import pdb;
from array import *
def find_dup(arr1):
    listt = []
    listtt = []
    count = 0
    for i in range(len(arr1)):
        if arr1[i] in listt and arr1[i] not in listtt:
            listtt.append(arr1[i])
        else:
            listt.append(arr1[i])   
    return listtt

array1 = array('i',[5,1,2,3,4,4,6,5,5,1,7,7,7,7,])
print (f"duplicate numbers are {find_dup(array1)}")
