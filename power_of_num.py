import pdb;
def power_num(num,power):
    if power<=0:
       return 1
    else:
        return (num * power_num(num,power-1))
print(power_num(2,4))
        