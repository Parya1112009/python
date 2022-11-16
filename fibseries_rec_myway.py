import pdb;
def fibno(a,b,n,list = []):
    
    if n < 1:
        return 1
    else:
        c = a+b
        list.append(c)
        #pdb.set_trace()
        fibno(b,c,n-1)   
    return list        
c = fibno(0,1,10)
print (c)