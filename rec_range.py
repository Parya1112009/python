import pdb;
def rec_range(num):
    if num==0:
       return 0
    else:
        return (num + rec_range(num-1))  
print(rec_range(6))
         