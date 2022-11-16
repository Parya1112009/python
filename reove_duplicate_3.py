def removeDuplicates(myList):
    new_list=[]
    new_listt=[]
 
    for i in myList:
 
        if i not in new_list:
 
            new_list.append(i)

        elif i not in new_listt:
             
             new_listt.append(i)

    return new_list, new_listt
print (removeDuplicates([1,3,2,1,4,5,2,1,3]))    
