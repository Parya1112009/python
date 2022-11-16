import pdb;
def fibno(k):
    if k < 1:
        return 1
    else:
        #pdb.set_trace()
        return (fibno(k-1) + fibno(k-2)) 
number = input("enter the number")           
for i in range(int(number)):
    print (fibno(i))

