import pdb;
def fibno(k):
    list = []
    if k < 1:
        return 1
    else:
        #pdb.set_trace()
        return list.append(fibno(k-1) + fibno(k-2))
number = input("enter the number")           
print (fibno(int(number)))


