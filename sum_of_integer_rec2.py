import pdb;
def sum_num(num):
    if num>0:
        #pdb.set_trace()
        rem = num%10
        num = num/10   
        num = int(num)
        return (rem + sum_num(num))
    else:
       return 0   
   
print(sum_num(5789))
        