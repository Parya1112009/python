import pdb;
def dtob(num,listt = []):
    if num==0:
       return listt
    else:
        listt.append(str(num%2))
        dtob(int(num/2))
        return (''.join(listt))
print(dtob(40))
        