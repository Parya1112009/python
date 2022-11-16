import pdb;
def sum_num(num):
    if num<=0:
       return 0
    else:
        return (num%10 + sum_num(int(num/10)))
print(sum_num(5789))
        