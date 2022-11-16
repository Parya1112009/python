name = "priyanka"
list = ["priyanla","arya","yuvan"]
list[1] = "eva"
print (name[0:6:2])
print (list)
list.reverse()
print(list)
string = "my,name,is,priya"
list2 = string.split(",")
print (list2)
string2 = "--".join(list2)
string3 = "@".join("priyanka")
print (string2)
print (string3)
list3 = ["my","son","is","yuvan"]
temp1,temp2,*temp3 = list3
print (temp1,temp2,temp3)
