import pdb;
def fibno(k,ite = []):
    if k in [0,1]:
        ite.append(k)
        return ite
    else:
        #pdb.set_trace()
        pdb.set_trace()
        c = (fibno(k-1) + fibno(k-2)) 
        ite.extend(c)
        return ite
number = input("enter the number")           
c = fibno(int(number))
print (c)
