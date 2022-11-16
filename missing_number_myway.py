import pdb;
def missing_num(listt):
    #pdb.set_trace()
    for i in range(1,10):
        #pdb.set_trace()
        if i != listt[i-1]:
            break
    return i
missing_number = missing_num([1,2,3,4,5,7,8,9,10])  
print (f"missing number in the list is {missing_number}")  