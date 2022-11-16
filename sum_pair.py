import pdb;
def pair_two(listt):
    total = []
    for i in range(0, len(listt)):
        for jo in  range(1, len(listt)):
            if (listt[i] + listt[jo] == 9) and ([listt[jo],listt[i]]) not in total: 
                total.append([listt[i], listt[jo]])
    return total            
pair_sum = pair_two([1,2,3,4,5,6,7,8,9,10])  
print (f"pair no with total 9 in the list is {pair_sum}")  