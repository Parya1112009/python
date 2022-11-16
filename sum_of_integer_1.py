def sum_num(num):
    sum = 0
    nu = str(num)
    for n in nu:
        if int(n) <= 0:
            return None
        else:
            sum += int(n)  
    return sum
print (sum_num(976))            