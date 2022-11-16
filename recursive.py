def num(n):
    if n<1:
        print("n is less than 1")
    else:
        num(n-1)
        print (n)    
number = input("enter the number")
print (num(int(number)))     