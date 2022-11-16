import pdb;
def missing_num(listt,no):
    #pdb.set_trace()
    sum1= no*(no+1)/2
    sum2 = sum(listt)
    return (int(sum1)-int(sum2))
missing_number = missing_num([1,2,3,4,5,7,8,9,10],10)  
print (f"missing number in the list is {missing_number}")  