import pdb;
def find_max(listt):
    #pdb.set_trace()
    if len(listt)== 1:
       return listt[0]
    else:
        return  max(listt[len(listt)-1], find_max(listt[0:-1]))
print(find_max([198,4,2,6,56,43,24,22]))
        