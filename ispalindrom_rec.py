import pdb;
def is_palin(stri):
    if len(stri) == 0:
       return True
    if stri[0] != stri[len(stri)-1]:
        return False
    else:
        pdb.set_trace()
        return is_palin(stri[1:-1])
name = input("enter the name")
pdb.set_trace()

print(is_palin(name))
         