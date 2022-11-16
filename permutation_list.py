def perm(listt1,listt2):
    if len(listt1)!=len(listt2):
        return False
    listt1.sort()
    listt2.sort()
    if (listt1 == listt2):
        return True
    else:
        return False
permutation = perm([1,2,3],[1,2,3])  
print(permutation)              

