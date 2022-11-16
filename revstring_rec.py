import pdb;
def rev_string(stri):
    
    #pdb.set_trace()
    if len(stri)== 1:
       return stri[0]
    else:
        return (stri[len(stri)-1] + rev_string(stri[0:len(stri)-1]))
name = input("enter the name")
print(rev_string(name))
         