def add_thrice(val,list=[]):
    list.append(val)
    list.append(val)
    list.append(val)
    return list  
def add_thrice2(val,list=None):
    if list == None:
       list = []    
       list.append(val)
       list.append(val)
       list.append(val)
    return list       
final_list = add_thrice(20,[2,3,4])  
print (f"the final list is {final_list}\n\n")
final_list2 = add_thrice(20) 
print (f"the final list2 after sending only one arg is {final_list2}")
final_list3 = add_thrice(21)
print (f"the final list3 after sending only one arg is {final_list3} which means its appending to the same list list2\n\n")
final_list4 = add_thrice2(200)
print (f"the solution of the list3 is declaring list as  none rather than taking it as empty so the resulted list is {final_list4}")
final_list5 = add_thrice2(300)
print (f"the solution of the list3 is declaring list as  none rather than taking it as empty so the resulted list is {final_list5}")