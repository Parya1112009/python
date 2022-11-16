def sum(*nos):
    total = 0
    for n in nos:
        total = total+n
    return total
list = [2,3,4,5,6,7] 
tot = sum(*list)   
list2 = [*list,78,89,90]
print (list2)
list3 = [list,55,66,77]
print(list3)
print (f"the total is {tot}")