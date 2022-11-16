import pdb;
def sum_num(num):
    #pdb.set_trace()
    sum = 0
    while num > 0:
        #pdb.set_trace()
        rem = num%10
        num = num/10   
        num = int(num) 
        sum += int(rem)  
    return sum
print(sum_num(9857))
        